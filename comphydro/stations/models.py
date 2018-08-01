from django.db import models
from django.utils.translation import gettext_lazy as _

class Coordinate(models.Model):
    class Meta:
        verbose_name_plural = _("Coordinates")
        verbose_name = _("Coordinate")
    x = models.FloatField()
    y = models.FloatField()


class Localization(models.Model):
    class Meta:
        verbose_name_plural = _("Localizations")
        verbose_name = _("Localization")
    coordinates = models.ForeignKey(Coordinate, models.CASCADE, verbose_name=_('coordinates'))
    """
    coordenadas = models.PointField(srid=4326)
    objects = models.GeoManager()
    """

    def __str__(self):
        return '%s %s' % (self.coordinates.x, self.coordinates.y)

    

'''#################### **************** POSTO *************** #####################'''

class StationType(models.Model):
    type = models.CharField(verbose_name=_('type'),max_length=20)
    class Meta:
        verbose_name_plural = _("Station Types")
        verbose_name = _("Station type")
    def __str__(self):
        return _('%(type)s')%{'type':self.type}
    
    
class Source(models.Model):
    class Meta:
        verbose_name_plural = _("Sources")
        verbose_name = _("Source")
    source = models.CharField(max_length=15)
    def __str__(self):
        return _('%(source)s')%{'source':self.source}

class Station(models.Model):
    class Meta:
        verbose_name_plural = _("Stations")
        verbose_name = _("Station")
    station_type = models.ForeignKey(StationType, models.CASCADE, verbose_name=_('station type'))
    source = models.ForeignKey(Source, models.CASCADE, verbose_name=_('source'))
    code = models.CharField(max_length=15,null=True,verbose_name=_('code'))
    name = models.CharField(max_length=100,verbose_name=_('name'))
    localization = models.ForeignKey(Localization, models.CASCADE, verbose_name=_('localization'))
    def __str__(self):
        return '%s %s (%s)'%(self.name,self.source.source,self.code)
    

