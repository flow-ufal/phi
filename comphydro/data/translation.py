from modeltranslation.translator import translator, TranslationOptions
from .models import Discretization,Variable,ConsistencyLevel

class DiscretizationTranslationOptions(TranslationOptions):
    fields = ('type',)
    
class VariableTranslationOptions(TranslationOptions):
    fields = ('variable',)
    
class ConsistencyLevelTranslationOptions(TranslationOptions):
    fields = ('type',)

translator.register(Discretization, DiscretizationTranslationOptions)
translator.register(Variable, VariableTranslationOptions)
translator.register(ConsistencyLevel, ConsistencyLevelTranslationOptions)
