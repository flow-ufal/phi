# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from data.models import Discretization,OriginalSerie,TemporalSerie,Stats
from django.contrib.postgres.fields import ArrayField

class Reduction(models.Model):
    type = models.CharField(max_length=20,verbose_name = _('type'))
    stats_type = models.ForeignKey(Stats, models.CASCADE, verbose_name = _('stats type'))
    hydrologic_year_type = models.CharField(max_length=50,choices=(('flood','flood'),('drought','drought')),verbose_name = _('hydrologic year type'))
    class Meta:
        verbose_name_plural = _("Reductions")
        verbose_name = _("Reduction")
    def __str__(self):
        return '%s'%self.type
     
class ReducedSerie(models.Model):
    original_serie = models.ForeignKey(OriginalSerie, models.CASCADE, verbose_name = _('original serie'))
    discretization = models.ForeignKey(Discretization, models.CASCADE, verbose_name = _('discretization'))
    reduction = models.ForeignKey(Reduction, models.CASCADE, verbose_name = _('reduction'))
    temporal_serie_id = models.IntegerField(verbose_name = _('temporal serie id'))
    limiar=models.FloatField(null=True,verbose_name = _('limiar'))
    class Meta:
        verbose_name_plural = _("Reduced Series")
        verbose_name = _("Reduced Serie")
    def __str__(self):
        return _('%(discretization)s %(reduction)s Serie from %(station)s station')%{'reduction':self.reduction.type,
                                                                                     'discretization':self.discretization.type,
                                                                                     'station':self.original_serie.station}
    
    
class Distribution(models.Model):
    """This class manages probability distributions"""
    name = models.CharField(max_length=100, verbose_name=_('name'))
    abreviation = models.CharField(max_length=5, verbose_name=_('abreviation'))

class ProbabilityCurve(models.Model):
    """This class manages probability curves"""
    distribution = models.ForeignKey(Distribution, models.CASCADE, verbose_name=_('distribution'))
    alpha = models.FloatField(verbose_name=_('alpha'))
    betha = models.FloatField(verbose_name=_('betha'))
    kappa = models.FloatField(verbose_name=_('kappa'))

    @property
    def parameters(self):
        return {"alpha": self.alpha, "betha": self.betha, 'kappa': self.kappa}

class ResamplingSerie(models.Model):
    """This class manages resampling series"""
    length = models.IntegerField(verbose_name=_('length'))
    curve = models.ForeignKey(ProbabilityCurve, models.CASCADE, verbose_name=_('curve'))
    data = ArrayField(models.FloatField(), verbose_name=_('data'))
    probabilities = ArrayField(models.FloatField(), verbose_name=_('probabilities'),blank=True)
    is_base_curve = models.BooleanField(verbose_name=_('Is base curve'))
