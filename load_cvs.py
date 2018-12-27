import sys
import os
import django

sys.path.append("D:/Files/PyCharm Projects/phi")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phi.settings")
django.setup()

import pandas as pd
import requests

from odm2.models import CvActionType
from odm2.models import CvAggregationStatistic
from odm2.models import CvAnnotationType
from odm2.models import CvCensorCode
from odm2.models import CvDataQualityType
from odm2.models import CvDataSetType
from odm2.models import CvDirectiveType
from odm2.models import CvElevationDatum
from odm2.models import CvEquipmentType
from odm2.models import CvMethodType
from odm2.models import CvOrganizationType
from odm2.models import CvPropertyDataType
from odm2.models import CvQualityCode
from odm2.models import CvRelationshipType
from odm2.models import CvResultType
from odm2.models import CvMedium
from odm2.models import CvSamplingFeatureGeoType
from odm2.models import CvSamplingFeatureType
from odm2.models import CvSiteType
from odm2.models import CvSpatialOffsetType
from odm2.models import CvSpeciation
# from odm2.models import CvSpecimenMedium
from odm2.models import CvSpecimenType
from odm2.models import CvStatus
from odm2.models import CvTaxonomicClassifierType
from odm2.models import CvUnitsType
from odm2.models import CvVariableName
from odm2.models import CvVariableType

from odm2.models import Units


django.setup()

url = 'http://vocabulary.odm2.org/api/v1/%s/?format=json'

vocabulary_list = [('actiontype', CvActionType),
                   ('aggregationstatistic', CvAggregationStatistic),
                   ('annotationtype', CvAnnotationType),
                   ('censorcode', CvCensorCode),
                   ('dataqualitytype', CvDataQualityType),
                   ('datasettype', CvDataSetType),
                   ('directivetype', CvDirectiveType),
                   ('elevationdatum', CvElevationDatum),
                   ('equipmenttype', CvEquipmentType),
                   ('medium', CvMedium),
                   ('methodtype', CvMethodType),
                   ('organizationtype', CvOrganizationType),
                   ('propertydatatype', CvPropertyDataType),
                   ('qualitycode', CvQualityCode),
                   ('relationshiptype', CvRelationshipType),
                   ('resulttype', CvResultType),
                   ('samplingfeaturegeotype', CvSamplingFeatureGeoType),
                   ('samplingfeaturetype', CvSamplingFeatureType),
                   ('sitetype', CvSiteType),
                   ('spatialoffsettype', CvSpatialOffsetType),
                   ('speciation', CvSpeciation),
                   ('specimentype', CvSpecimenType),
                   ('status', CvStatus),
                   ('taxonomicclassifiertype', CvTaxonomicClassifierType),
                   ('unitstype', CvUnitsType),
                   ('variablename', CvVariableName),
                   ('variabletype', CvVariableType),
                   ]

extra = [('units', Units)]

for vocabulary in vocabulary_list:
    data = requests.get(url % vocabulary[0]).json()['objects']
    df = pd.DataFrame.from_dict(data)

    for i in range(len(df)):
        term = df['term'][i]
        name = df['name'][i]
        definition = df['definition'][i]
        category = df['category'][i]
        sourcevocabularyuri = df['resource_uri'][i]

        obj = vocabulary[1](term=term, name=name, definition=definition, category=category, sourcevocabularyuri=sourcevocabularyuri)
        obj.save()
    print(vocabulary[0], 'done.')
