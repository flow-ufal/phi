from scipy.stats import genpareto, genextreme#kstest, chisquare, anderson
from lmoments3 import distr
functions_fit = {'gev-mvs':genextreme.fit,'gev-lmom':distr.gev.lmom_fit}
inverse_by_distribution = {'gev':genextreme.ppf}

class FrequencyAnalysis(object):
    '''This funtion manages the frequency analysis'''
    def __init__(self,distribution):
        self.distribution = distribution
    def estimate_parameters(self,data,estimator):
        parameters = functions_fit['%s-%s'%(self.distribution.abreviation, estimator.abreviation)](data)
        if hasattr(parameters,'values'):
            return list(parameters.values())
        return parameters

    def estimates_magnitudes(self, probabilities, parameters):
        data = [
            inverse_by_distribution[self.distribution.abreviation](
                p,
                parameters['kappa'],
                loc=parameters['alpha'],
                scale=parameters['betha']) for p in probabilities]
        return data