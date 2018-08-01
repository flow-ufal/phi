"""comphydro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
#from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns


 
urlpatterns = [
    url('i18n/', include('django.conf.urls.i18n')),
]
 
urlpatterns += i18n_patterns(
    url('admin/', admin.site.urls),
    url('stations/', include('stations.urls')),
    url('', include('stations.urls')),
    url('stats/', include('stats.urls')),
)
