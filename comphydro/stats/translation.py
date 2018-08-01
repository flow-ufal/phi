from modeltranslation.translator import translator, TranslationOptions
from .models import Reduction, ReducedSerie, Distribution, ProbabilityCurve, ResamplingSerie

class ReductionTranslationOptions(TranslationOptions):
    fields = ('type',)
    
    


translator.register(Reduction, ReductionTranslationOptions)