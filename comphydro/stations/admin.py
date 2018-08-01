from django.contrib import admin

from .models import Station, Source, StationType, Localization,Coordinate

class StationTypeAdmin(admin.ModelAdmin):
    model = StationType
    list_display = ['type']
    search_fields = ['type']
    save_on_top = True
    
    
class SourceAdmin(admin.ModelAdmin):
    model = Source
    list_display = ['source']
    search_fields = ['source']
    save_on_top = True
    
    
class LocalizationAdmin(admin.ModelAdmin):
    model = Localization
    list_display = ['coordinates']
    save_on_top = True
    
    
class StationAdmin(admin.ModelAdmin):
    model = Station
    list_display = ['name','station_type','source','code','localization']
    search_fields = ['name']
    save_on_top = True

admin.site.register(StationType,StationTypeAdmin)
admin.site.register(Coordinate)
admin.site.register(Station,StationAdmin)
admin.site.register(Localization,LocalizationAdmin)
admin.site.register(Source,SourceAdmin)