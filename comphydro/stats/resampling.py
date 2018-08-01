from random import uniform
from .frequency import FrequencyAnalysis
from .models import Distribution, ResamplingSerie, ProbabilityCurve

class Resampling(object):
    def get_distribution(self,abreviation='gev'):
        distributions = Distribution.objects.all()
        if not distributions:
            gev = Distribution.objects.create(name="Generalized Extreme Value",abreviation="gev")
            gev.save()
        return Distribution.objects.get(abreviation=abreviation)


    def get_curve(self,parameters, distribution):
        curve = ProbabilityCurve.objects.filter(distribution=distribution).filter(
            alpha=parameters['alpha']).filter(betha=parameters['betha']).filter(
                kappa=parameters['kappa']
            )
        if not curve:
            curve = ProbabilityCurve.objects.create(distribution=distribution,**parameters)
            curve.save()
        else:
            curve=curve[0]
        return curve

    def data_from_curve(self, curve, n=None, probabilities=[]):
        stats = FrequencyAnalysis(curve.distribution)
        if not n is None:
            probabilities = [uniform(0,1) for i in range(n)]
        print(probabilities)
        return stats.estimates_magnitudes(probabilities, curve.parameters), probabilities

    def create_resampling_serie(self, curve, data, n, is_base_curve=False,probabilities=[]):
        serie = ResamplingSerie.objects.create(length=n, curve=curve, data=data, is_base_curve=is_base_curve, probabilities=probabilities)
        serie.save()
        return serie
    def resampling_from_parameters(self, parameters, distribution_abreviation='gev',n=None,probabilities=[]):
        distribution = self.get_distribution(distribution_abreviation)
        curve = self.get_curve(parameters,distribution)
        if not probabilities and n is None:
            return "Error",False
        serie = ResamplingSerie.objects.filter(curve=curve).filter(length=n)
        if serie:
            return serie
        data, probabilities = self.data_from_curve(curve, n, probabilities)
        return self.create_resampling_serie(curve, data, n, is_base_curve=True, probabilities=probabilities)