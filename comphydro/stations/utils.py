from furl import furl
import pandas as pd

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language,gettext as _

from data.models import Discretization,Unit,Variable,ConsistencyLevel,OriginalSerie,TemporalSerie
from data.graphs import plot_web
from stats.forms import GenericStatsForm,IHAForm,AnnualStatsForm
#from stats.stats import Stats

from .forms import CreateStationForm
from .models import Station, Source, StationType, Localization,Coordinate
from .reads_data import ANA,ONS


def get_daily_from_temporal(temporals,start_year=None,end_year=None):
    data = [o.data if not o is None else nan for o in temporals]
    date = [o.date for o in temporals]
    df = pd.DataFrame({"data" : data}, index=pd.DatetimeIndex(date))
    gp = pd.Grouper(freq='D',sort=True)
    df = df.groupby(gp).mean()
    if not start_year is None:
        df = df[df.index.year>=start_year]
    if not end_year is None:
        df = df[df.index.year<=end_year]
    return df


class Stats(object):
    def __init__(self,request,name,short_name,variables,form,stats=None):
        data = request.POST if short_name in request.POST else None
        self.name = name        
        if stats is None:
            self.form=form(variables=variables,stats_type=" ".join(short_name.split("_")),data=data,prefix=short_name)
        else:
            self.form=form(variables=variables,stats_list=stats,data=data,prefix=short_name)
        self.short_name=short_name
        
annual_stats_strings = {
                         'rate_of_change':_("Rate of change"),
                         'reference_flow':_("Reference Flow"),
                         'frequency_of_change':_("Frequency of change"),
                         'julian_date':_("Julian Date"),
                         'pulse_count':_("Pulse Count"),
                         'pulse_duration':_("Pulse Duration"),

                }

basic_stats_strings = {
                'basic_stats':_("Basic Stats"),
}

rolling_mean_stats_strings = {
                'rolling_mean':_("Rolling Mean"),
                         
}


specific_stats_strings={'iha':"IHA"}


def get_specific_stats(request,variables):
    return [
        Stats(request,_("Indicators of Hydrologic Alterations"),'iha',variables,IHAForm),
    ]

list_all_stats = [basic_stats_strings,rolling_mean_stats_strings,annual_stats_strings,specific_stats_strings]

def get_all_stats_form_list():
    all_stats={}
    for data_stats in list_all_stats:
        for key,value in data_stats.items():
            all_stats[key]=value
    return ((key,all_stats[key]) for key in all_stats)


def get_standard_stats_form_list():
    t=[]
    for key,value in basic_stats_strings.items():
        t.append((key,value))
        
    for key,value in rolling_mean_stats_strings.items():
        t.append((key,value))
        
    return tuple(t)




def get_annual_stats_form_list():
    return ((key,annual_stats_strings[key]) for key in annual_stats_strings)

def get_specific_stats_form_list():
    return ((key,specific_stats_strings[key]) for key in specific_stats_strings)

        
def get_stats_list(request,variables):
    l = []
    l.extend([Stats(request,basic_stats_strings[key],key,variables,GenericStatsForm) for key in basic_stats_strings])
    l.extend([Stats(request,rolling_mean_stats_strings[key],key,variables,GenericStatsForm) for key in rolling_mean_stats_strings])
    #l.append(Stats(request,_("Annual Statistics"),"annual_stats",variables,AnnualStatsForm,get_annual_stats_form_list()))
    l.extend(get_specific_stats(request,variables))
    return l

class StationInfo(object):
    def __init__(self,station_id,*variables):
        self.station=Station.objects.get(id=station_id)
        if variables:
            self.variable_ids=list(map(int,[v for v in variables if not v is None]))
        
        
    def update_originals(self,Serie=OriginalSerie):
        if self.variable_ids:
            self.originals = OriginalSerie.objects.filter(station=self.station)
            self.originals.filter(variable__id__in=self.variable_ids)
        else:
            self.originals = OriginalSerie.objects.filter(station=self.station)
    def update_variables_and_sources(self):
        if self.variable_ids:
            self.variables=Variable.objects.filter(id__in=self.variable_ids)
        else:
            self.variables=list(set([o.variable for o in self.originals]))
        self.sources=list(set([o.station.source for o in self.originals]))
        return self.originals,self.variables,self.sources
    def create_daily_data_pandas(self,temporals):
        self.temporals = temporals
        self.daily_data = get_daily_from_temporal(temporals)
        return self.daily_data
    def create_graph(self,xys,variable,unit):
        return plot_web(xys=xys,
                                      title="%s"%(str(variable)),
                                        variable=variable,unit=unit)
    def get_originals_graphs_and_temporals(self):
        self.update_originals()
        self.update_variables_and_sources()
        for original in self.originals:
            temporals = TemporalSerie.objects.filter(id=original.temporal_serie_id) 
            original.temporals = temporals
            daily_data=self.create_daily_data_pandas(temporals)
            self.xys=[[daily_data.index,daily_data['data'].values],]
            original.graph = self.create_graph(self.xys,original.variable,original.unit)
            
            
            