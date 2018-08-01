# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from .models import Source, StationType


class CreateStationForm(forms.Form):
    """Choices"""
    station_types = ((tipo.id,tipo.type) for tipo in StationType.objects.all())
    sources = ((fonte.id,fonte.source) for fonte in Source.objects.all())
    
    """Campos do Formulário"""
    station_type = forms.ChoiceField(label=_("Station Type:"),choices=station_types,widget=forms.Select(attrs={'class':'form-control'}))
    source = forms.ChoiceField(label=_("Source:"),choices=sources,widget=forms.Select(attrs={'class':'form-control'}))
    ana_code = forms.CharField(label=_("ANA Code:"),required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    