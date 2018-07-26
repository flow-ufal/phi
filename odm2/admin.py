from django.contrib import admin

from .models import ActionBy
from .models import Actions
from .models import Affiliations
from .models import AuthorLists
from .models import CitationExtensionPropertyValues
from .models import Citations
from .models import DataloggerFileColumns
from .models import DataloggerFiles
from .models import DataloggerProgramFiles
from .models import DataQuality
from .models import DatasetCitations
from .models import Datasets
from .models import DatasetsResults
from .models import DerivationEquations
from .models import EquipmentModels
from .models import ExtensionProperties
from .models import ExternalIdentifierSystems
from .models import FeatureActions
from .models import InstrumentOutputVariables
from .models import MeasurementResults
from .models import MeasurementResultValues
from .models import MethodCitations
from .models import Methods
from .models import Organizations
from .models import People
from .models import PersonExternalIdentifiers
from .models import ProcessingLevels
from .models import ProfileResults
from .models import ProfileResultValues
from .models import RelatedActions
from .models import RelatedFeatures
from .models import RelatedResults
from .models import Results
from .models import ResultsDataQuality
from .models import ResultDerivationEquations
from .models import SamplingFeatureExternalIdentifiers
from .models import SamplingFeatures
from .models import Sites
from .models import SpatialReferences
from .models import TaxonomicClassifiers
from .models import TimeSeriesResults
from .models import TimeSeriesResultValues
from .models import Units
from .models import Variables


# <editor-fold desc="ODM2Core">

admin.site.register(ActionBy)
admin.site.register(Actions)
admin.site.register(Affiliations)
admin.site.register(Datasets)
admin.site.register(DatasetsResults)
admin.site.register(FeatureActions)
admin.site.register(Methods)
admin.site.register(Organizations)
admin.site.register(People)
admin.site.register(ProcessingLevels)
admin.site.register(RelatedActions)
admin.site.register(Results)
admin.site.register(SamplingFeatures)
admin.site.register(TaxonomicClassifiers)
admin.site.register(Units)
admin.site.register(Variables)

# </editor-fold>

# <editor-fold desc="ODM2Equipment">

admin.site.register(DataloggerFileColumns)
admin.site.register(DataloggerFiles)
admin.site.register(DataloggerProgramFiles)
admin.site.register(EquipmentModels)
admin.site.register(InstrumentOutputVariables)

# </editor-fold>

#  <editor-fold desc="ODM2Provenance">

admin.site.register(AuthorLists)
admin.site.register(Citations)
admin.site.register(DatasetCitations)
admin.site.register(DerivationEquations)
admin.site.register(MethodCitations)
admin.site.register(RelatedResults)
admin.site.register(ResultDerivationEquations)

# </editor-fold>

# <editor-fold desc="ODM2DataQuality">

admin.site.register(DataQuality)
admin.site.register(ResultsDataQuality)

# </editor-fold>

# <editor-fold desc="ODM2ExtensionProperties">

admin.site.register(CitationExtensionPropertyValues)
admin.site.register(ExtensionProperties)

# </editor-fold>

# <editor-fold desc="ODM2ExternalIdentifiers">

admin.site.register(ExternalIdentifierSystems)
admin.site.register(PersonExternalIdentifiers)
admin.site.register(SamplingFeatureExternalIdentifiers)

# </editor-fold>

# <editor-fold desc="ODM2SamplingFeatures">

admin.site.register(RelatedFeatures)
admin.site.register(Sites)
admin.site.register(SpatialReferences)

# </editor-fold>

#  <editor-fold desc="ODM2Results">

admin.site.register(MeasurementResults)
admin.site.register(MeasurementResultValues)
admin.site.register(ProfileResults)
admin.site.register(ProfileResultValues)
admin.site.register(TimeSeriesResults)
admin.site.register(TimeSeriesResultValues)

# </editor-fold>
