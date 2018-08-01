# -*- coding: utf-8 -*-
from six import add_metaclass
import pandas as pd
from numpy import nan, mean, argmax, argmin, where, split, std
from datetime import datetime
from abc import ABCMeta, abstractmethod
from django.utils.translation import gettext as _
from data.models import *
from data.graphs import plot_web, plot_polar
from stations.reads_data import get_id_temporal, criar_temporal
from stations.models import Station
from stations.utils import StationInfo, get_daily_from_temporal
from .models import Reduction, ReducedSerie

funcoes_reducao = {
    'máxima': max, 'mínima': min, 'soma': sum, 'média': mean, 'máxima média móvel': argmax,
    'mínima média móvel': argmin, 'fall rate': '>', 'rise rate': '<',
    'fall count': '>', 'rise count': '<', 'low count': '<',
    'high count': '>', 'low duration': '<', 'high duration': '>'
    }
meses = {
    1: "JAN", 2: "FEB", 3: "MAR", 4: "APR", 5: "MAY", 6: "JUN",
    7: "JUL", 8: "AUG", 9: "SEP", 10: "OCT", 11: "NOV", 12: "DEC"
    }

reduction_abreviations = {'maximum':'max', 'minimum':'min'}

def get_originals(variables, originals):
    os = []
    for variable in variables:
        originals_by_variable = [o for o in originals if o.variable==variable]
        cl_data_type = 'consisted' if 'consisted' in [o.consistency_level.type_en_us for o in originals_by_variable] else 'raw'
        os.append([o for o in originals_by_variable if o.consistency_level.type_en_us == cl_data_type][0])
    return os

def get_daily_data(station, variable, start_year=None, end_year=None):
    originals = OriginalSerie.objects.filter(station=station)
    originals = get_originals([variable,], originals)
    temporals = TemporalSerie.objects.filter(id=originals[0].temporal_serie_id)
    return get_daily_from_temporal(temporals, start_year, end_year)

class Table:
    def __init__(self, title, pre_data, pos_data):
        self.title = title
        self.pre_data = pre_data
        self.pos_data = pos_data
        self.deviation_magnitude = pos_data-pre_data
        if pre_data == 0:
            self.percent =- 100
        else:
            self.percent = int(self.deviation_magnitude/pre_data*100)

    def __str__(self):
        return str(self.title)+"  -  "+str(self.value)

class generic_obj:
    pass

def get_available_variables(station):
    return [o.variable for o in OriginalSerie.objects.filter(station=station)]


@add_metaclass(ABCMeta)
class BaseStats(StationInfo):
    plot_daily = False
    plot_permancence_curve = False
    def get_parameters(self, temporal_data, reduction, parameters):
        return {}

    def update_informations(self, discretization_code=None, reduction_id=None, stats_type='standard'):
        if discretization_code is None:
            discretizations = Discretization.objects.all()
            discretizations = [d for d in discretizations if d.stats_type.type==stats_type]
            if not discretizations:
                discretizations = Discretization.objects.filter(type_en_us='annual')
            self.discretizations = discretizations
        else:
            self.discretizations = Discretization.objects.filter(pandas_code=discretization_code)
        if reduction_id == None:
            self.reductions = Reduction.objects.filter(stats_type__type=stats_type)
        else:
            self.reductions = Reduction.objects.filter(id=reduction_id)

    def update_originals(self):
        super(BaseStats, self).update_originals()
        self.update_variables_and_sources()
        self.originals = get_originals(self.variables, self.originals)
        return self.originals

    def starting_month_hydrologic_year(self, df):
        mean_by_month = df["data"].groupby(pd.Grouper(freq='M')).mean()
        years_minimum = df.groupby(pd.Grouper(freq='AS')).idxmin()
        return pd.value_counts([d.month for d in years_minimum["data"]]).idxmax()

    def hydrologic_years_dict(self, df, hydrologic_year_type="flood"):
        n_month = self.starting_month_hydrologic_year(df)
        if hydrologic_year_type != 'flood':
            n_month += 6
            if n_month > 12:
                n_month -= 12
        gp = df["data"].groupby(pd.Grouper(freq="AS-%s"%meses[n_month]))
        dic = dict(list(gp))
        annual_dic = {key: dic[key] for key in dic.keys()}
        '''        for key in dic.keys():
            df_year=pd.DataFrame({'data':dic[key].values,'hyear':[key for i in dic[key].index]},index=dic[key].index)
            hydrologic_years.append(df_year)
        df=pd.concat(hydrologic_years)
        print(df)'''
        return annual_dic

    def get_reduced_serie(self, original, discretization, reduction, limiar=None):
        return ReducedSerie.objects.filter(
                original_serie = original, discretization=discretization, reduction=reduction, limiar=limiar)

    @abstractmethod
    def reduce(self):
        pass

    def get_or_create_reduced_data(self,daily,original,discretization,reduction,limiar=None,median=None,start_year=0,end_year=9999):
        reduced = self.get_reduced_serie(
            original, discretization, reduction, limiar)
        if reduced:
            temporal_data = TemporalSerie.objects.filter(
                id = reduced[0].temporal_serie_id)
            reduced = reduced[0]
        else:
            date, data = self.reduce(daily, discretization, reduction, limiar, median)
            temporal_data, reduced = self.get_temporal_data(
                original, discretization, reduction, data, date, limiar)
        reduced.temporals = [t for t in temporal_data if start_year <= t.date.year <= end_year]
        date = [t.date for t in reduced.temporals]
        data = [t.data for t in reduced.temporals]
        return reduced, date, data

    def get_graphs_data(self, daily, original, discretization):
        graph = generic_obj()
        reduceds = []
        xys = []
        graph.parameters = {}
        for reduction in self.reductions:
            self.get_parameters(daily, reduction, graph.parameters)
            reduced, x, y = self.get_or_create_reduced_data(daily, original, discretization, reduction)
            reduceds.append(reduced)
            xys.append([x, y])
        names = [r.type for r in self.reductions]
        if self.plot_daily:
            xys.append([list(daily.index.to_datetime()), [d[0] for d in daily.values]])
            names.append(_('daily_data'))
        graph.variable = original.variable
        graph.discretization = discretization
        graph.reduceds = reduceds
        graph.xys = xys
        graph.names = names
        return graph, names

    def create_graph(self, xys, variable, unit, discretization, names):
        '''
        This method is responsible to return the graph. To change the graph.
        '''
        return plot_web(xys=xys, title=_("%(discretization)s %(variable)s")%
                                                {'variable': str(variable),
                                                 'discretization':str(discretization)
                                                 },
                                            variable=variable, unit=unit, names=names)

    def get_or_create_reduced_series(self):
        self.update_originals()
        self.update_variables_and_sources()
        self.reduceds = []
        graphs = []
        for original in self.originals:
            temporals = TemporalSerie.objects.filter(id=original.temporal_serie_id)
            daily = self.create_daily_data_pandas(temporals)
            anos_hidrologicos = self.hydrologic_years_dict(daily)
            discretizations = self.discretizations[:]
            for discretization in discretizations:
                graph, names = self.get_graphs_data(daily, original, discretization)
                if graph.xys:
                    graph.graph = self.create_graph(graph.xys, original.variable, original.unit, discretization, names)
                    graphs.append(graph)
            if self.plot_permancence_curve:
                xys = self.get_permancence_curve_data(daily)
                graph=generic_obj()
                graph.graph = plot_web(xys, _('Permanence Curve'),original.variable,original.unit,[_('data'),],'%')
                graph.title=_('Permanence Curve')
                graphs.append(graph)
        self.reduceds = graphs
        return self.reduceds

    def get_temporal_data(self,original,discretization,reduction,dados,datas,limiar=None):
        id = criar_temporal(dados,datas)
        reduced_serie = ReducedSerie.objects.create(
                original_serie = original,
                discretization = discretization,
                reduction = reduction,
                temporal_serie_id = id,
            limiar=limiar
        )
        reduced_serie.save()
        return TemporalSerie.objects.filter(id=id),reduced_serie

class BasicStats(BaseStats):
    plot_daily=True
    def reduce(self,daily,discretization,reduction,limiar=None,median=None):
        gp = pd.Grouper(freq=discretization.pandas_code)
        discretized = daily.groupby(gp).agg(funcoes_reducao[reduction.type_pt_br])
        discretized.index = pd.DatetimeIndex(
            [d[0] for d in eval("daily.groupby(gp).idx%s().values"%reduction_abreviations[reduction.type_en_us])]
        )
        date = list(discretized.index)
        data = list(discretized["data"])
        return date,data

class RollingMean(BaseStats):
    plot_daily=True
    def reduce(self,daily,discretization,reduction,limiar=None,median=None):
        daily_rolling_mean = daily.rolling(window=int(discretization.pandas_code),center=False).mean()
        hydrologic_years = self.hydrologic_years_dict(daily_rolling_mean,reduction.hydrologic_year_type)
        gp = pd.Grouper(freq="10AS")
        years = sorted(list(hydrologic_years.keys())[1:])
        data = [hydrologic_years[year].groupby(gp).agg(funcoes_reducao[reduction.type_pt_br]).max()
                 for year in years if not hydrologic_years[year].groupby(gp).agg(funcoes_reducao[reduction.type_pt_br]) is (nan)]
        date = [pd.to_datetime(eval("hydrologic_years[year].groupby(gp).idx%s().values"%reduction_abreviations[reduction.type_en_us])[0])
                 for year in years  if not hydrologic_years[year].groupby(gp).agg(funcoes_reducao[reduction.type_pt_br]) is (nan)]
        return date,data




class ReferenceFlow(BaseStats):

    plot_permancence_curve=True

    def get_permancence_curve_data(self,daily):
        x=[i/1000 for i in range(1001)]
        y = [daily.quantile(1-i).values[0] for i in x]
        return  [[x,y],]

    def get_parameters(self,daily,reduction,parameters):
        parameters['Q50'] = daily.quantile(q=0.5, numeric_only=True).values[0]
        parameters['Q90'] = daily.quantile(q=0.1, numeric_only=True).values[0]
        parameters['Qbase'] = parameters['Q90']/parameters['Q50']

    def reduce(self,daily,discretization,reduction,limiar=None,median=None):
        daily['month']=[o.month for o in daily.index]
        mean_by_month = daily.groupby('month').quantile(q=0.05, numeric_only=True)
        data = [d[0] for d in mean_by_month.values]
        date = [datetime(1900,m,1) for m in set(daily['month'].values)]
        return date,data



@add_metaclass(ABCMeta)
class BaseAnnualEvents(BaseStats):

    calculate_limiar=False

    @abstractmethod
    def get_reduced_value(self,df,reduction):
        pass

    def reduce(self,daily,discretization,reduction,limiar=None,median=None):
        hydrologic_years = self.hydrologic_years_dict(daily,reduction.hydrologic_year_type)
        years = sorted(list(hydrologic_years.keys())[1:])
        data = []
        if not all([limiar is None,median is None]):
            self.median=median
            self.limiar=limiar
        if all([self.calculate_limiar,limiar is None,median is None]):
            self.median = daily.median().values[0]
            self.limiar = daily.quantile(quantils[reduction.hydrologic_year_type]).values[0]
        for year in years:
            df = hydrologic_years[year]
            df=pd.DataFrame({'data':df.values},index=df.index)
            data.append(float(self.get_reduced_value(df,reduction)))
        date = [datetime(year.year,1,1) for year in years]
        return date,data


class RateOfChange(BaseAnnualEvents):

    def create_graph(self,xys,variable,unit,discretization,names):
        return plot_web(xys=xys,title=_("%(discretization)s %(variable)s")%
                                                {'variable':_('rate of change'),
                                                 'discretization':str(discretization)
                                                 },
                                            variable=_('rate'),unit='m³/s/dia',names=names)

    def get_reduced_value(self,df,reduction):
        df['dif'] = df['data'] - df['data'].shift(1)
        values = df[eval("df['dif']"+funcoes_reducao[reduction.type_en_us]+'0')]['dif']
        return values.mean()


class FrequencyOfChange(BaseAnnualEvents):

    def create_graph(self,xys,variable,unit,discretization,names):
        return plot_web(xys=xys,title=_("%(discretization)s %(variable)s")%
                                                {'variable':_('frequency of change'),
                                                 'discretization':str(discretization)
                                                 },
                                            variable=_('frequency'),unit='un',names=names)

    def get_reduced_value(self,df,reduction):
        df['dif_unit'] = (df['data'] - df['data'].shift(1))/abs(df['data'] - df['data'].shift(1))
        events = split(df['dif_unit'], where(eval("df['dif_unit']"+funcoes_reducao[reduction.type_en_us]+"df['dif_unit'].shift(1)"))[0])
        return len(events)


quantils = {'flood':0.75,'drought':0.25}

class PulseCount(BaseAnnualEvents):
    calculate_limiar=True


    def get_parameters(self,daily,reduction,parameters):
        parameters['median'] = daily.median().values[0]
        parameters['%s limiar '%str(reduction)] = daily.quantile(quantils[reduction.hydrologic_year_type]).values[0]

    def get_reduced_value(self, df, reduction):
        limiar=self.limiar
        m = self.median
        df['num'] = [i for i in range(len(df))]
        eventoM = df[eval("df['data'] "+funcoes_reducao[reduction.type_en_us]+"= m")]
        eventoM=eventoM.dropna()
        eventoM['dif'] = eventoM['num'] - eventoM['num'].shift(1)
        events = split(eventoM['data'], where(eventoM['dif']>1)[0])
        eventsL=[]
        for event in events:
            eL=event[eval("event "+funcoes_reducao[reduction.type_en_us]+"= limiar")].dropna()
            index = list(eL.index)
            if index:
                eventsL.append({'initial_date':index[0],'final_date':index[-1],'data':eL.values})
        return len(eventsL)

class PulseDuration(BaseAnnualEvents):
    calculate_limiar=True

    def get_parameters(self,daily,reduction,parameters):
        parameters['median'] = daily.median().values[0]
        parameters['%s limiar '%str(reduction)] = daily.quantile(quantils[reduction.hydrologic_year_type]).values[0]
    def get_reduced_value(self, df, reduction):
        limiar=self.limiar
        m = self.median
        df['num'] = [i for i in range(len(df))]
        eventoM = df[eval("df['data'] "+funcoes_reducao[reduction.type_en_us]+"= m")].dropna()
        eventoM['dif'] = eventoM['num'] - eventoM['num'].shift(1)
        events = split(eventoM['data'], where(eventoM['dif']>1)[0])
        eventsL=[]
        for event in events:
            eL=event[eval("event "+funcoes_reducao[reduction.type_en_us]+"= limiar")].dropna()
            index = list(eL.index)
            if index:
                eventsL.append({'initial_date':index[0],'final_date':index[-1],'data':eL.values})
        difs=[(e['final_date']-e['initial_date']) for e in eventsL]
        difs=[e.days for e in difs]
        if difs:
            return sum(difs)/len(difs)
        return 0


class JulianDate(BaseAnnualEvents):
    def create_graph(self,xys,variable,unit,discretization,names):
        return plot_polar(xys=xys,title=_("%(discretization)s %(variable)s")%
                                                {'variable':_('Rate'),
                                                 'discretization':str(discretization)
                                                 },
                                            variable=_('julian date'),unit='day',names=names)

    def get_reduced_value(self,df,reduction):

        date_maximum = pd.DatetimeIndex(eval('df.idx%s().values'%reduction_abreviations[reduction.type_en_us]))[0]
        julian = date_maximum-datetime(date_maximum.year,1,1)
        return julian.days




















month_names=[_('January'),_('February'),_('March'),_('April'),
                     _('May'),_('June'),_('July'),_('August'),_('September'),
                     _('October'),_('November'),_('December')]


def get_mothly_data(daily_data):
    daily_data['month']=[o.month for o in daily_data.index]
    mean_by_month = daily_data.groupby('month').mean()
    return [round(d[0],2) for d in mean_by_month.values]

def get_limiar(df,quantile):
    return df.quantile(quantile).values[0]

def get_median(df):
    return df.median().values[0]
def cv(data):
    m = mean(data)
    if m==0:
        return 0
    return std(data)/mean(data)






class IHA:
    def __init__(self,station_id,other_id,variable=None,start_year=None,end_year=None):
        self.station = Station.objects.get(id=station_id)
        other = Station.objects.filter(id=other_id)
        if other:
            self.other=other[0]
        else:
            self.other=Station.objects.latest('id')
        if variable==None:
            self.variable = Variable.objects.get(variable_en_us="flow")
        else:
            self.variable = Variable.objects.get(id=variable)
        self.start_year=int(start_year) if not start_year is None else 0
        self.end_year=int(end_year) if not end_year is None else 9999
        self.original = {
            'pre_data':get_originals([self.variable,],OriginalSerie.objects.filter(station=self.station))[0],
            'pos_data':get_originals([self.variable,],OriginalSerie.objects.filter(station=self.other))[0]}
        self.daily = {}
        for type_data in self.original:
            temporals = TemporalSerie.objects.filter(id=self.original[type_data].temporal_serie_id)
            self.daily[type_data] = get_daily_from_temporal(temporals,self.start_year,self.end_year)
        self.annual_discretization = Discretization.objects.get(type_en_us="annual")
        discretizations = list(Discretization.objects.filter(stats_type__type = 'rolling mean'))
        discretizations.sort(key=lambda x:int(x.pandas_code))
        self.rolling_mean_discretizations=discretizations

    def get_data(self,classes,discretization,title,function_reduce=mean,calculate_limiar=False):
        datas=[]
        for type_classe in classes:
            for reduction in Reduction.objects.filter(stats_type__type = type_classe):
                data_mean = {}
                if calculate_limiar:
                    daily = self.daily['pre_data']
                    limiar = get_limiar(daily,quantils[reduction.hydrologic_year_type])
                    median = get_median(daily)
                else:
                    limiar,median=None,None
                for type_data in self.original:
                    stat = classes[type_classe](self.original[type_data].station.id,self.original[type_data].variable.id)
                    reduced,date,data = stat.get_or_create_reduced_data(
                        self.daily[type_data],self.original[type_data],discretization,reduction,limiar,median,self.start_year,self.end_year)
                    data_mean[type_data]=round(function_reduce(data),2)
                line = Table(title %
                                 {'reduction':reduction.type,
                                  'discretization':discretization.type},
                                 data_mean['pre_data'],
                                 data_mean['pos_data'],
                )
                datas.append(line)
        return datas

    def ReferenceFlow(self):
        data={}
        xys=[]
        names=[]
        for type_data in self.daily:
            daily=self.daily[type_data]
            daily['month']=[o.month for o in daily.index]
            mean_by_month = daily.groupby('month').quantile(q=0.05, numeric_only=True)
            data[type_data] = [d[0] for d in mean_by_month.values]
            date = pd.DatetimeIndex([datetime(1900,m,1) for m in set(daily['month'].values)])
            xys.append([date,data[type_data]])
            names.append(type_data)

        graph=plot_web(xys=xys,title=_("Reference Flow"),
                                    variable=_("Flow"),unit="m³/s",names=names)

        return [Table(month_names[i],data['pre_data'][i],data['pos_data'][i]) for i in range(12)],graph

    def Group1(self):
        data={}
        for type_data in self.daily:
            data[type_data] = get_mothly_data(self.daily[type_data])
        return [Table(month_names[i],data['pre_data'][i],data['pos_data'][i]) for i in range(12)]



    def Group2(self):
        datas=[]
        discretizations = list(Discretization.objects.filter(stats_type__type = 'rolling mean'))
        discretizations.sort(key=lambda x:int(x.pandas_code))
        graphs=[]
        for discretization in discretizations:
            for reduction in Reduction.objects.filter(stats_type__type = 'rolling mean'):
                data_mean = {}
                xys=[]
                names=[]

                for type_data in self.daily:
                    daily_data = self.daily[type_data]
                    basic_stats = RollingMean(self.station.id,self.variable.id)
                    reduced,date,data = basic_stats.get_or_create_reduced_data(
                        self.daily[type_data],self.original[type_data],discretization,reduction,None,None,self.start_year,self.end_year)
                    mean_=round(sum(data)/len(data),2)
                    xys.append([date,data])
                    names.append(type_data)
                    xys.append([[date[0],date[-1]],[mean_,mean_]])
                    names.append(type_data+" "+_("mean"))
                    data_mean[type_data]=mean_

                graph=plot_web(xys=xys,title=_("%(discretization)s %(variable)s %(reduction)s")%
                                                {'variable':str(self.variable),
                                                 'discretization':str(discretization),
                                                 'reduction':str(reduction.type)
                                                 },
                                            variable=self.variable,unit="m³/s",names= names)

                graphs.append(graph)
                line = Table('Annual %(reduction)s %(discretization)s means' %
                             {'reduction':reduction.type,
                              'discretization':discretization.type},
                             data_mean['pre_data'],
                             data_mean['pos_data'],
                )
                datas.append(line)
        return datas,graphs

    def Group(self,classes,string='%(reduction)s',function_reduce=mean,calculate_limiar=False):
        '''This is a geral method to get the data of Groups 3-5 (annual parameters)'''
        return self.get_data(classes,self.annual_discretization,string,function_reduce,calculate_limiar)


    def Group1cv(self):
        data={}
        for type_data in self.daily:
            daily_data = self.daily[type_data]
            daily_data['month']=[o.month for o in daily_data.index]
            mean_by_month = daily_data.groupby('month').mean()
            std_by_month = daily_data.groupby('month').std()
            cv_by_month = std_by_month/mean_by_month
            months = [d for d in cv_by_month.index]
            data[type_data] = [round(d[0],2) for d in cv_by_month.values]
        return [Table(month_names[i],data['pre_data'][i],data['pos_data'][i]) for i in range(12)]

    def Group2cv(self):
        datas=[]
        discretizations = list(Discretization.objects.filter(stats_type__type = 'rolling mean'))
        discretizations.sort(key=lambda x:int(x.pandas_code))
        graphs=[]
        for discretization in discretizations:
            for reduction in Reduction.objects.filter(stats_type__type = 'rolling mean'):
                data_mean = {}
                xys=[]
                names=[]

                for type_data in self.daily:
                    daily_data = self.daily[type_data]
                    basic_stats = RollingMean(self.station.id,self.variable.id)
                    reduced,date,data = basic_stats.get_or_create_reduced_data(
                        self.daily[type_data],self.original[type_data],discretization,reduction,None,None,self.start_year,self.end_year)
                    mean_=sum(data)/len(data)
                    std_ = std(data)
                    cv = std_/mean_
                    data_mean[type_data]=round(cv,2)
                    xys.append([date,data])
                    names.append(type_data)
                    xys.append([[date[0],date[-1]],[mean_,mean_]])
                    names.append(type_data+" "+_("mean"))

                graph=plot_web(xys=xys,title=_("%(discretization)s %(variable)s %(reduction)s")%
                                                {'variable':str(self.variable),
                                                 'discretization':str(discretization),
                                                 'reduction':str(reduction.type)
                                                 },
                                            variable=self.variable,unit="m³/s",names= names)

                graphs.append(graph)
                line = Table('Annual %(reduction)s %(discretization)s means' %
                             {'reduction':reduction.type,
                              'discretization':discretization.type},
                             data_mean['pre_data'],
                             data_mean['pos_data'],
                )
                datas.append(line)
        return datas,graphs
