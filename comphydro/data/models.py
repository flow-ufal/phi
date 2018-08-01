# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from stations.models import Station, Source, StationType, Localization,Coordinate



class TemporalSerie(models.Model):
    Id = models.AutoField(primary_key=True)
    id = models.IntegerField(unique=False)
    data = models.FloatField(null=True,verbose_name = _('data'))
    date = models.DateTimeField(verbose_name = _('date and time'),unique=False)
    
    class Meta:
        unique_together = (("id","date"),)
        verbose_name_plural = _("Temporal Series")
        verbose_name = _("Temporal Serie")
        

class Stats(models.Model):
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.type
    type = models.CharField(max_length=50,verbose_name = _('type'))
    class Meta:
        verbose_name_plural = _("Stats")
        verbose_name = _("Stats") 

class Discretization(models.Model):
    type = models.CharField(max_length=30,verbose_name = _('type'))
    pandas_code = models.CharField(max_length=20,verbose_name = _('pandas code'))
    stats_type = models.ForeignKey(Stats, models.CASCADE, verbose_name = _('stats type'))
    class Meta:
        verbose_name_plural = _("Discretizations")
        verbose_name = _("Discretization")
    def __str__(self):
        return '%s'%self.type
    
    
class Unit(models.Model):
    unit = models.CharField(max_length=20,verbose_name = _('unit'))
    class Meta:
        verbose_name_plural = _("Metric Units")
        verbose_name = _("Metric Unit")
    def __str__(self):
        return '%s'%self.unit
    
    
class Variable(models.Model):
    variable = models.CharField(max_length=20,verbose_name = _('variable'))
    ana_code = models.CharField(max_length=2,verbose_name = _('ANA code'))
    class Meta:
        verbose_name_plural = _("Variables")
        verbose_name = _("Variable")
    def __str__(self):
        return '%s'%self.variable
    
    
class ConsistencyLevel(models.Model):
    type = models.CharField(max_length=20,verbose_name = _('type'))
    class Meta:
        verbose_name_plural = _("Levels of consistency")
        verbose_name = _("Level of consistency")
    def __str__(self):
        return '%s'%self.type
    
    
'''#################### **************** ORIGINAL SERIE *************** #####################'''

class OriginalSerie(models.Model):
    station = models.ForeignKey(Station, models.CASCADE, verbose_name=_('station'))
    date_file_source = models.DateTimeField(auto_now_add=True,verbose_name=_('date and time'),unique=False)
    variable = models.ForeignKey(Variable, models.CASCADE, verbose_name=_('variable'))
    consistency_level = models.ForeignKey(ConsistencyLevel, models.CASCADE, verbose_name=_('level of consistency'))
    discretization = models.ForeignKey(Discretization, models.CASCADE, verbose_name=_('discretization'))
    unit = models.ForeignKey(Unit, models.CASCADE)
    temporal_serie_id = models.IntegerField()
    def __str__(self):
        return _('Original Serie from %s data from %s station, with %s (%s) data') % (self.discretization.type,
                                                                                      self.station,self.variable,self.unit)
    class Meta:
        verbose_name_plural = _("Original Series")
        verbose_name = _("Original Serie")