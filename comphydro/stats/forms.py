# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from data.models import Discretization,OriginalSerie
from stations.models import Station
from .models import Distribution
 
    

class GenericStatsForm(forms.Form):
    def __init__(self, variables=[],stats_type="standard", *args, **kwargs):
        super(GenericStatsForm, self).__init__(*args, **kwargs)
        self.fields['variable'].choices =list(variables)
        ds = Discretization.objects.filter(stats_type__type=stats_type)
        if not ds:
            ds=Discretization.objects.filter(stats_type__type="standard")
        discretizations = ((discretizacao.pandas_code,discretizacao.type) 
                          for discretizacao in ds)
        self.fields['discretization'].choices =list(discretizations)

    variable = forms.ChoiceField(label=_("Data type")+":",widget=forms.Select(attrs={'class':'form-control'}))
    discretization = forms.ChoiceField(label=_("Discretization")+":",required=False,
                                         widget=forms.Select(attrs={'class':'form-control'}))
    
    
class AnnualStatsForm(forms.Form):
    def __init__(self, variables=[],stats_list=[], *args, **kwargs):
        super(AnnualStatsForm, self).__init__(*args, **kwargs)
        self.fields['variable'].choices =list(variables)
        self.fields['stats'].choices =list(stats_list)
        

    variable = forms.ChoiceField(label=_("Data type")+":",widget=forms.Select(attrs={'class':'form-control'}))
    stats = forms.ChoiceField(label=_("Stats")+":",required=False,
                                         widget=forms.Select(attrs={'class':'form-control'}))
    


    
    
class IHAForm(forms.Form):
    def __init__(self, variables=[],stats_type="standard", *args, **kwargs):
        super(IHAForm, self).__init__(*args, **kwargs)
    station = forms.ChoiceField(label=_("Station to compare")+":",widget=forms.Select(attrs={'class':'form-control'}),choices=
                                 ((o.id,o) for o in Station.objects.all())
                                )
    initial = forms.CharField(label=_("Initial year")+":",widget=forms.TextInput(attrs={'class':'form-control'}))
    final = forms.CharField(label=_("Final year")+":",widget=forms.TextInput(attrs={'class':'form-control'}))


class SerieFromParametersForm(forms.Form):
    probability_or_aleatory = forms.ChoiceField(label=_("Probability Values or Aleatory?")+":",required=False,widget=forms.Select(attrs={'class':'form-control'}),choices=
                                 ((1,_("Probabilities")),(2,_("Aleatory"))))
    probability_values = forms.CharField(label=_("Values of probability (numbers separateds by commas)")+":",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    sample_size = forms.IntegerField(label=_("Size of sample")+":",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    distribution = forms.ChoiceField(label=_("Distribution")+":",widget=forms.Select(attrs={'class':'form-control'}),choices=
                                 ((distribution.abreviation, distribution.name) for distribution in Distribution.objects.all()))
    alpha = forms.FloatField(label=_("Apha")+":",widget=forms.TextInput(attrs={'class':'form-control'}))
    betha = forms.FloatField(label=_("Betha")+":",widget=forms.TextInput(attrs={'class':'form-control'}))
    kappa = forms.FloatField(label=_("Kappa")+":",widget=forms.TextInput(attrs={'class':'form-control'}))

