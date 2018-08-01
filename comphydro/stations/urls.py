from django.conf.urls import include, url
from .views import create_station,stations,StationInformation

urlpatterns =(
    url(r'^new$', create_station,name="create_station"),
    url(r'^$', stations,name="stations"),
    url(r'^(?P<station_id>[^/]+)/information/(?P<filters>.*)$', StationInformation.as_view(),name="station_information"),
)