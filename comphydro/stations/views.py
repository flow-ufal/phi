from furl import furl
import pandas as pd

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language,gettext as _

from data.models import Discretization,Unit,Variable,ConsistencyLevel,OriginalSerie,TemporalSerie
from data.graphs import plot_web,plot_map
#from stats.forms import RollingMeanForm,BasicStatsForm,RateFrequencyOfChangeForm,IHAForm
from .utils import Stats

from .forms import CreateStationForm
from .models import Station, Source, StationType, Localization,Coordinate
from .reads_data import ANA,ONS,Chesf
from .utils import StationInfo,get_all_stats_form_list,get_stats_list



from django.views import View

class StationInformation(View):
    '''This class '''

    context = {"BASE_URL":""}

    def get_filters(self,filters):
        return furl("?"+filters).args
    def get_info_and_variables(self,station_id,filters):
        info = StationInfo(station_id,filters.get('variavel_id',None))
        info.get_originals_graphs_and_temporals()
        variables=[(variable.id,variable.variable) for variable in info.variables]
        self.context['sources']=info.sources
        self.context['originals']=info.originals
        self.context['station']=info.originals[0].station
        self.context['variables']=variables


    def get(self, request, *args, **kwargs):
        filters = self.get_filters(kwargs['filters'])
        self.get_info_and_variables(kwargs['station_id'],filters)
        self.context['stats'] = get_stats_list(request,self.context['variables'])
        self.context['all_stats'] = all_stats = get_all_stats_form_list()
        return render(request,'station_information.html',self.context)



    def post(self, request, *args, **kwargs):
        filters = self.get_filters(kwargs['filters'])
        self.get_info_and_variables(kwargs['station_id'],filters)
        stats = get_stats_list(request,self.context['variables'])
        valid_stats = [stat for stat in stats if stat.form.is_valid()]
        if len(valid_stats)>0:
            form = valid_stats[0].form
            data=form.cleaned_data
            url = furl("")
            keys = {
                'variable':data.get('variable',None),'discretization':data.get('discretization',None),
                'start_year':data.get("initial",None),'end_year':data.get("final",None),"other_id":data.get('station',None)
                       }
            keys = {key:value for key,value in keys.items() if not value is None}
            url.args = keys


            return HttpResponseRedirect("/%s/stats/%s/%s/%s"%(get_language(),valid_stats[0].short_name,kwargs['station_id'],url.url.replace("?","")))
        return self.get(request, *args, **kwargs)


def create_station(request):
    if request.method == 'POST':
        form =CreateStationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("formulário validado")
            station_type = StationType.objects.get(id=data["station_type"])
            source = Source.objects.get(id=data["source"])
            code = data["ana_code"]
            print("code")
            postos = Station.objects.filter(code=code)
            if postos:
                messages.add_message(request, messages.ERROR, _('The station of code: %s already exists into the database.')%postos[0].code)
                return render(request,'create_station.html',{'aba':'map','form':form})
            print('Solicitando Hidroweb')
            hid = eval(source.source)()
            print(source.source)
            name,localization,erro = hid.obtem_nome_e_localizacao_posto(code)
            if erro:
                messages.add_message(request, messages.ERROR, '%s'%name)
                return render(request,'create_station.html',{'aba':'map','form':form})
            station = Station.objects.create(station_type=station_type,source=source,code=code,name=name, localization=localization)
            station.save()

            for codigo_variavel in range(9,10):
                variavel = Variable.objects.get(ana_code=codigo_variavel)
                executa = hid.executar(station,variavel)
                if executa:
                    messages.add_message(request, messages.ERROR, '%s'%executa)
            messages.add_message(request, messages.SUCCESS, 'Concluído!')
            return render(request,'create_station.html',{'aba':'map'})
    form =CreateStationForm
    return render(request,'create_station.html',{'aba':'map','form':form})


def stations(request):
    lat,lon,text=[],[],[]
    station_list = Station.objects.all()
    context={'BASE_URL':"",'stations':stations}
    if station_list:
        for station in station_list:
            text.append('<a href="/%s/stations/%d/information">%s</a>'%(get_language(),station.id,station))
            lat.append(station.localization.coordinates.y)
            lon.append(station.localization.coordinates.x)

        context['graph'] = plot_map(lat,lon,text)

    return render(request,'stations.html',context)
