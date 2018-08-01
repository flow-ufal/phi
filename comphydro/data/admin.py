# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Discretization,Unit,Variable,ConsistencyLevel,OriginalSerie,Stats

class UnitAdmin(admin.ModelAdmin):
    model = Unit
    list_display = ['unit']
    search_fields = ['unit']
    save_on_top = True

class StatsAdmin(admin.ModelAdmin):
    model = Stats
    list_display = ['type']
    search_fields = ['type']
    save_on_top = True

class VariableAdmin(admin.ModelAdmin):
    model = Variable
    list_display = ['variable']
    search_fields = ['variable']
    save_on_top = True
    
class ConsistencyLevelAdmin(admin.ModelAdmin):
    model = ConsistencyLevel
    list_display = ['type']
    search_fields = ['type']
    save_on_top = True
class DiscretizationAdmin(admin.ModelAdmin):
    model = Discretization
    list_display = ['type']
    search_fields = ['type']
    save_on_top = True

class OriginalSerieAdmin(admin.ModelAdmin):
    model = OriginalSerie
    #list_display = ['Discretizacao_','Unidade_','Variavel_','Tipo_Dado_','serie_Temporal_id']
    list_display = ['temporal_serie_id','station','discretization','variable','unit','consistency_level']
    search_fields = ['temporal_serie_id']
    save_on_top = True
    
admin.site.register(Unit,UnitAdmin)
admin.site.register(Stats,StatsAdmin)
admin.site.register(Variable,VariableAdmin)
admin.site.register(ConsistencyLevel,ConsistencyLevelAdmin)
admin.site.register(Discretization,DiscretizationAdmin)
admin.site.register(OriginalSerie,OriginalSerieAdmin)