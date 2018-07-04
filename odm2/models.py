# Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

import uuid

from django.db import models
from django.db.models import UUIDField

# from django.db.models import Manager as GeoManager
# from django.contrib.gis.geos import GEOSGeometry


# <editor-fold desc="ODM2CV">

class CvActionType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_actiontype'
        ordering = ['term', 'name']


class CvAggregationStatistic(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_aggregationstatistic'
        ordering = ['term', 'name']


class CvAnnotationType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_annotationtype'
        ordering = ['term', 'name']


class CvCensorCode(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_censorcode'
        ordering = ['term', 'name']


class CvDataQualityType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_dataqualitytype'
        ordering = ['term', 'name']


class CvDataSetType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_datasettype'
        ordering = ['term', 'name']


class CvDirectiveType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_directivetype'
        ordering = ['term', 'name']


class CvElevationDatum(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_elevationdatum'
        verbose_name = 'elevation datum'
        ordering = ['term', 'name']


class CvEquipmentType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_equipmenttype'
        ordering = ['term', 'name']


class CvMethodType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_methodtype'
        ordering = ['term', 'name']


class CvOrganizationType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_organizationtype'
        ordering = ['term', 'name']


class CvPropertyDataType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_propertydatatype'
        ordering = ['term', 'name']


class CvQualityCode(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_qualitycode'
        ordering = ['term', 'name']


class CvRelationshipType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_relationshiptype'
        ordering = ['term', 'name']


class CvResultType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_resulttype'
        ordering = ['term', 'name']


class CvMedium(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_medium'
        ordering = ['term', 'name']


class CvSamplingFeatureGeoType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturegeotype'
        verbose_name = 'sampling feature geo type'
        ordering = ['term', 'name']


class CvSamplingFeatureType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_samplingfeaturetype'
        verbose_name = 'sampling feature type'
        ordering = ['term', 'name']


class CvSiteType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_sitetype'
        ordering = ['term', 'name']


class CvSpatialOffsetType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_spatialoffsettype'
        ordering = ['term', 'name']


class CvSpeciation(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_speciation'
        ordering = ['term', 'name']


class CvSpecimenMedium(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_medium'
        ordering = ['term', 'name']


class CvSpecimenType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_specimentype'
        ordering = ['term', 'name']


class CvStatus(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_status'
        ordering = ['term', 'name']


class CvTaxonomicClassifierType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_taxonomicclassifiertype'
        ordering = ['term', 'name']
        verbose_name = "taxonomic classifier"


class CvUnitsType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_unitstype'
        ordering = ['term', 'name']


class CvVariableName(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        managed = False
        db_table = 'cv_variablename'
        ordering = ['term', 'name']


class CvVariableType(models.Model):
    term = models.CharField(max_length=255)
    name = models.CharField(primary_key=True, max_length=255)
    definition = models.CharField(max_length=1000, blank=True)
    category = models.CharField(max_length=255, blank=True)
    sourcevocabularyuri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'cv_variabletype'
        ordering = ['term', 'name']

# </editor-fold>


# <editor-fold desc="ODM2Core">

class ActionBy(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey('Actions', verbose_name="action", db_column='actionid', on_delete=models.CASCADE)
    affiliationid = models.ForeignKey('Affiliations', verbose_name="person by affiliation",
                                      db_column='affiliationid', on_delete=models.CASCADE)
    isactionlead = models.BooleanField(verbose_name="is lead person on action")
    roledescription = models.CharField(max_length=5000, verbose_name="person's role on this action",
                                       blank=True)

    def __str__(self):
        s = self.actionid
        if self.affiliationid:
            s += " - %s" % self.affiliationid
        if self.roledescription:
            s += " - %s" % self.roledescription
        return s

    class Meta:
        managed = False
        db_table = 'actionby'
        verbose_name = 'action by'
        verbose_name_plural = 'action by'


class Actions(models.Model):
    actionid = models.AutoField(primary_key=True)
    actiontypecv = models.ForeignKey('CvActionType',
                                     help_text='A vocabulary for describing the type of actions '
                                              'performed in making observations. Depending'
                                              ' on the action type, the action may or may not '
                                              'produce an observation result. view action type '
                                              'details here http://vocabulary.odm2.org/actiontype/',
                                     db_column='actiontypecv', on_delete=models.CASCADE)
    method = models.ForeignKey('Methods', db_column='methodid', on_delete=models.CASCADE)
    begindatetime = models.DateTimeField(verbose_name='begin date time')
    begindatetimeutcoffset = models.IntegerField(
        verbose_name='begin date time clock off set (from GMT)', default=4)
    enddatetime = models.DateTimeField(verbose_name='end date time', blank=True, null=True)
    enddatetimeutcoffset = models.IntegerField(
        verbose_name='end date time clock off set (from GMT)', default=4)
    actiondescription = models.CharField(verbose_name='action description', max_length=5000,
                                         blank=True)
    actionfilelink = models.CharField(verbose_name='action file link', max_length=255, blank=True)

    def __str__(self):
        s = self.actiontypecv
        if self.method:
            s += " | %s" % self.method
        if self.method:
            s += " | %s" % (self.actiondescription[:25])
        return s

    class Meta:
        managed = False
        db_table = 'actions'
        verbose_name = 'action'


class Affiliations(models.Model):
    afiliationid = models.AutoField(primary_key=True)
    personid = models.ForeignKey('People', verbose_name='person', db_column='personid', on_delete=models.CASCADE)
    organizationid = models.ForeignKey('Organizations', verbose_name='organization',
                                       db_column='organizationid',
                                       blank=True, null=True, on_delete=models.CASCADE)
    isprimaryorganizationcontact = models.NullBooleanField(
        verbose_name='primary organization contact? ')
    affiliationstartdate = models.DateField(verbose_name="When affiliation began ")
    affiliationenddate = models.DateField(verbose_name="When affiliation ended", blank=True,
                                          null=True)
    primaryphone = models.CharField(verbose_name="primary phone", max_length=50, blank=True)
    primaryemail = models.CharField(verbose_name="primary email", max_length=255)
    primaryaddress = models.CharField(verbose_name="primary address", max_length=255, blank=True)
    personlink = models.CharField(max_length=255, blank=True)

    def __str__(self):
        s = self.personid
        if self.organizationid:
            s += " | %s" % self.organizationid
        return s

    class Meta:
        managed = False
        db_table = 'affiliations'
        verbose_name = 'affiliation (relate people and organizations)'
        verbose_name_plural = 'affiliation (relate people and organizations)'
        ordering = ['-primaryemail']


class Datasets(models.Model):
    datasetid = models.AutoField(primary_key=True)
    datasetuuid = UUIDField(default=uuid.uuid4, editable=False)
    datasettypecv = models.ForeignKey(CvDataSetType, verbose_name="dataset type",
                                      db_column='datasettypecv',
                                      on_delete=models.CASCADE)
    datasetcode = models.CharField(verbose_name="dataset code", max_length=50)
    datasettitle = models.CharField(verbose_name="dataset title", max_length=255)
    datasetabstract = models.CharField(verbose_name="dataset abstract", max_length=5000)

    def __str__(self):
        s = self.datasetcode
        if self.datasettitle:
            s += " - %s" % self.datasettitle
        return s

    class Meta:
        managed = False
        db_table = 'datasets'
        verbose_name = 'dataset'


class DatasetsResults(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    datasetid = models.ForeignKey(Datasets, verbose_name="dataset", db_column='datasetid',
                                  on_delete=models.CASCADE)
    resultid = models.ForeignKey('Results', verbose_name="add the dataset to the result",
                                 db_column='resultid',
                                 on_delete=models.CASCADE)

    def __str__(self):
        s = self.datasetid
        if self.resultid:
            s += " - %s" % self.resultid
        return s

    class Meta:
        managed = False
        db_table = 'datasetsresults'
        verbose_name = 'dataset result'


class FeatureActions(models.Model):
    featureactionid = models.AutoField(primary_key=True, verbose_name="sampling feature action")
    samplingfeatureid = models.ForeignKey('SamplingFeatures', db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    action = models.ForeignKey(Actions, db_column='actionid',
                               on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %s" % (self.featureactionid, self.samplingfeatureid, self.action)

    class Meta:
        managed = False
        db_table = 'featureactions'
        verbose_name = 'action at sampling feature'
        verbose_name_plural = 'action at sampling feature'


class Methods(models.Model):
    methodid = models.AutoField(primary_key=True)
    methodtypecv = models.ForeignKey(CvMethodType, verbose_name='method type',
                                     help_text='A vocabulary for describing types of Methods '
                                               'associated with creating observations. '
                                               'MethodTypes correspond with ActionTypes in ODM2. '
                                               'An Action must be performed using an '
                                               'appropriate MethodType - e.g., a specimen '
                                               'collection Action should be associated with a '
                                               'specimen collection method. details for '
                                               'individual values '
                                               'here: http://vocabulary.odm2.org/methodtype/',
                                     db_column='methodtypecv',
                                     on_delete=models.CASCADE)
    methodcode = models.CharField(verbose_name='method code', max_length=50)
    methodname = models.CharField(verbose_name='method name', max_length=255)
    methoddescription = models.CharField(verbose_name='method description', max_length=5000,
                                         blank=True)
    methodlink = models.CharField(verbose_name='web link for method', max_length=255, blank=True)
    organizationid = models.ForeignKey('Organizations', verbose_name='organization',
                                       db_column='organizationid',
                                       blank=True, null=True,
                                       on_delete=models.CASCADE)

    def __str__(self):
        s = "%s" % self.methodcode
        if self.methodtypecv:
            s += ", %s" % self.methodtypecv
        return s

    class Meta:
        managed = False
        db_table = 'methods'
        verbose_name = 'method'
        ordering = ["methodname"]


class Organizations(models.Model):
    organizationid = models.AutoField(primary_key=True)
    organizationtypecv = models.ForeignKey(CvOrganizationType, verbose_name="organization type",
                                           db_column='organizationtypecv',
                                           on_delete=models.CASCADE)
    organizationcode = models.CharField(verbose_name="organization code", max_length=50)
    organizationname = models.CharField(verbose_name="organization name", max_length=255)
    organizationdescription = models.CharField(verbose_name="organization description",
                                               max_length=5000, blank=True)
    organizationlink = models.CharField(verbose_name="organization web link", max_length=255,
                                        blank=True)
    parentorganizationid = models.ForeignKey('self', verbose_name="parent organization",
                                             db_column='parentorganizationid', blank=True,
                                             null=True, default=1,
                                             on_delete=models.CASCADE)

    def __str__(self):
        s = self.organizationcode
        if self.organizationname:
            s += ", %s" % self.organizationname
        return s

    class Meta:
        managed = False
        db_table = 'organizations'
        verbose_name = 'organization'


class People(models.Model):
    personid = models.AutoField(primary_key=True)
    personfirstname = models.CharField(max_length=255, verbose_name="first name")
    personmiddlename = models.CharField(max_length=255, verbose_name="middle name", blank=True)
    personlastname = models.CharField(max_length=255, verbose_name="last name")

    def __str__(self):
        s = self.personlastname
        if self.personfirstname:
            s += ", %s" % self.personfirstname
        return s

    class Meta:
        managed = False
        db_table = 'people'
        verbose_name = 'people'
        verbose_name_plural = 'people'
        ordering = ["personlastname"]


class ProcessingLevels(models.Model):
    processinglevelid = models.AutoField(primary_key=True)
    processinglevelcode = models.CharField(verbose_name='processing level code', max_length=50)
    definition = models.CharField(max_length=5000, blank=True)
    explanation = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        s = "%s " % self.processinglevelcode
        if self.definition:
            s += ", %s" % self.definition
        return s

    class Meta:
        managed = False
        db_table = 'processinglevels'
        verbose_name = 'processing level'


class RelatedActions(models.Model):
    relationid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(Actions, verbose_name='action', db_column='actionid',
                                 on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, verbose_name='relationship type',
                                           db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedactionid = models.ForeignKey(Actions, verbose_name='related action',
                                        related_name='RelatedActions',
                                        db_column='relatedactionid',
                                        on_delete=models.CASCADE)

    def __str__(self):
        s = self.actionid
        if self.relationshiptypecv:
            s += ", %s" % self.relationshiptypecv
        if self.relatedactionid:
            s += ", %s" % self.relatedactionid
        return s

    class Meta:
        managed = False
        db_table = 'relatedactions'
        verbose_name = 'related action (associates one action with another)'
        verbose_name_plural = 'related action (associates one action with another)'


class Results(models.Model):
    resultid = models.AutoField(primary_key=True, verbose_name="data result")
    resultuuid = UUIDField(default=uuid.uuid4, editable=False)
    featureactionid = models.ForeignKey(FeatureActions, related_name="feature_actions",
                                        verbose_name="sampling feature action",
                                        db_column='featureactionid',
                                        on_delete=models.CASCADE)
    resulttypecv = models.ForeignKey(CvResultType, verbose_name='result type',
                                     db_column='resulttypecv',
                                     on_delete=models.CASCADE)
    variableid = models.ForeignKey('Variables', verbose_name='variable', db_column='variableid',
                                    on_delete=models.CASCADE)
    unitsid = models.ForeignKey('Units', verbose_name='units', related_name='+',
                                 db_column='unitsid',
                                 on_delete=models.CASCADE)
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifiers',
                                              verbose_name='taxonomic classifier',
                                              db_column='taxonomicclassifierid', blank=True,
                                              null=True,
                                              on_delete=models.CASCADE)
    processinglevelid = models.ForeignKey(ProcessingLevels, db_column='processinglevelid',
                                          on_delete=models.CASCADE)
    resultdatetime = models.DateTimeField(verbose_name='Start result date time', blank=True,
                                          null=True)
    resultdatetimeutcoffset = models.BigIntegerField(
        verbose_name='Start result date time UTC offset', default=4,
        null=True)
    # validdatetime>> Date and time for which the result is valid (e.g., for a forecast result).
    # Should probably be expressed as a duration
    validdatetime = models.DateTimeField(
        verbose_name='valid date time- Date and time for which the result is valid',
        blank=True, null=True)
    validdatetimeutcoffset = models.BigIntegerField(verbose_name='valid date time UTC offset',
                                                    default=4, null=True)
    statuscv = models.ForeignKey(CvStatus, verbose_name='status', db_column='statuscv', blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    sampledmediumcv = models.ForeignKey(CvMedium, verbose_name='sampled medium',
                                        db_column='sampledmediumcv',
                                        blank=True, null=True,
                                        on_delete=models.CASCADE)
    valuecount = models.IntegerField(verbose_name='number of recorded values')

    def __str__(self):
        return "%s - %s - ID: %s" % (self.variableid, self.featureactionid, self.resultid)

    class Meta:
        managed = False
        db_table = 'results'
        verbose_name = 'data result'
        ordering = ["variableid"]


class SamplingFeatures(models.Model):
    samplingfeatureid = models.AutoField(primary_key=True)
    samplingfeatureuuid = UUIDField(default=uuid.uuid4, editable=False)
    samplingfeaturetypecv = models.ForeignKey(CvSamplingFeatureType,
                                              db_column='samplingfeaturetypecv',
                                              on_delete=models.CASCADE)
    samplingfeaturecode = models.CharField(verbose_name='sampling feature or location code', max_length=50)
    samplingfeaturename = models.CharField(verbose_name='sampling feature or location name', max_length=255,
                                           blank=True, null=True)
    samplingfeaturedescription = models.CharField(verbose_name='sampling feature or location description',
                                                  max_length=5000,
                                                  blank=True)
    samplingfeaturegeotypecv = models.ForeignKey(CvSamplingFeatureGeoType,
                                                 db_column='samplingfeaturegeotypecv',
                                                 default="Point", null=True,
                                                 on_delete=models.CASCADE)
    featuregeometry = models.TextField(verbose_name='feature geometry', blank=True,
                                       null=True)  # GeometryField This field type is a guess.
    elevation_m = models.FloatField(verbose_name='elevation', blank=True, null=True)
    elevation_datum = models.ForeignKey(CvElevationDatum, db_column='elevationdatumcv', blank=True,
                                        null=True,
                                        on_delete=models.CASCADE)

    # objects = GeoManager()

    # def featuregeometrywkt(self):
    #    return GEOSGeometry(self.featuregeometry)

    featuregeometrywkt = models.CharField(max_length=8000, blank=True)

    def __str__(self):
        s = "%s - %s - %s" % (
            self.samplingfeaturecode, self.samplingfeatureid, self.samplingfeaturetypecv)
        if self.samplingfeaturename:
            s += " - %s" % self.samplingfeaturename
        return s

    class Meta:
        managed = False
        db_table = 'samplingfeatures'
        ordering = ('samplingfeaturetypecv', 'samplingfeaturename',)
        verbose_name = 'sampling feature (location)'


class TaxonomicClassifiers(models.Model):
    taxonomicclassifierid = models.AutoField(primary_key=True)
    taxonomicclassifiertypecv = models.ForeignKey(CvTaxonomicClassifierType,
                                                  db_column='taxonomicclassifiertypecv',
                                                  help_text="A vocabulary for describing "
                                                            "types of taxonomies from which "
                                                            "descriptive terms used "
                                                            "in an ODM2 database have been drawn. "
                                                            "Taxonomic classifiers provide "
                                                            "a way to classify"
                                                            " Results and Specimens "
                                                            "according to terms from a formal "
                                                            "taxonomy.. Check "
                                                            "http://vocabulary.odm2.org/"
                                                            "taxonomicclassifiertype/  "
                                                            "for more info",
                                                  on_delete=models.CASCADE)
    taxonomicclassifiername = models.CharField(verbose_name='taxonomic classifier name',
                                               max_length=255)
    taxonomicclassifiercommonname = models.CharField(
        verbose_name='taxonomic classifier common name', max_length=255,
        blank=True)
    taxonomicclassifierdescription = models.CharField(
        verbose_name='taxonomic classifier description', max_length=5000,
        blank=True)
    parenttaxonomicclassifierid = models.ForeignKey('self', db_column='parenttaxonomicclassifierid',
                                                    blank=True,
                                                    null=True,
                                                    on_delete=models.CASCADE)

    def __str__(self):
        s = self.taxonomicclassifiername
        if self.taxonomicclassifiercommonname:
            s += " - %s" % self.taxonomicclassifiercommonname
        return s

    class Meta:
        managed = False
        db_table = 'taxonomicclassifiers'
        verbose_name = 'taxonomic classifier'


class Units(models.Model):
    unitsid = models.AutoField(primary_key=True)
    unittypecv = models.ForeignKey(CvUnitsType,
                                   help_text="A vocabulary for describing the type of the Unit "
                                            "or the more general quantity that the Unit "
                                            "represents. View unit type details here "
                                            "http://vocabulary.odm2.org/unitstype/",
                                   db_column='unitstypecv',
                                   on_delete=models.CASCADE)
    unitsabbreviation = models.CharField(verbose_name='unit abbreviation', max_length=50)
    unitsname = models.CharField(verbose_name='unit name', max_length=255)
    unitslink = models.CharField(verbose_name='reference for the unit (web link)',
                                 max_length=255,
                                 blank=True)

    def __str__(self):
        s = self.unitsabbreviation
        if self.unitsname:
            s += " - %s" % self.unitsname
        return s

    class Meta:
        managed = False
        ordering = ('unitsabbreviation', 'unitsname',)
        db_table = 'units'
        verbose_name = 'unit'


class Variables(models.Model):
    variableid = models.AutoField(primary_key=True)
    variabletypecv = models.ForeignKey(CvVariableType,
                                       help_text="view variable types here "
                                                "http://vocabulary.odm2.org/variabletype/ ",
                                       db_column='variabletypecv',
                                       on_delete=models.CASCADE)
    variablecode = models.CharField(verbose_name='variable code', max_length=50)
    variablenamecv = models.ForeignKey(CvVariableName,
                                       help_text="view variable names here "
                                                "http://vocabulary.odm2.org/variablename/",
                                       db_column='variablenamecv',
                                       on_delete=models.CASCADE)
    variabledefinition = models.CharField(verbose_name='variable definition', max_length=500,
                                          blank=True)
    speciation = models.ForeignKey(CvSpeciation, db_column='speciationcv', blank=True, null=True,
                                   on_delete=models.CASCADE)
    nodatavalue = models.FloatField(verbose_name='no data value')

    def __str__(self):
        s = "%s" % self.variablecode
        if self.variabledefinition:
            s += " - %s" % self.variabledefinition[:20]
        return s

    class Meta:
        managed = False
        ordering = ('variablecode', 'variablenamecv',)
        db_table = 'variables'
        verbose_name = 'variable'

# </editor-fold>


# <editor-fold desc="ODM2Equipment">

class CalibrationActions(models.Model):
    actionid = models.OneToOneField(Actions, db_column='actionid', primary_key=True,
                                 on_delete=models.CASCADE)
    calibrationcheckvalue = models.FloatField(blank=True, null=True)
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariables',
                                                   db_column='instrumentoutputvariableid',
                                                   on_delete=models.CASCADE)
    calibrationequation = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = r'calibrationactions'


class CalibrationReferenceEquipment(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(CalibrationActions, db_column='actionid',
                                 on_delete=models.CASCADE)
    equipmentid = models.ForeignKey('Equipment', db_column='equipmentid',
                                 on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'calibrationreferenceequipment'


class CalibrationStandards(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(CalibrationActions, db_column='actionid',
                                 on_delete=models.CASCADE)
    referencematerialid = models.ForeignKey('ReferenceMaterials', db_column='referencematerialid',
                                            on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'calibrationstandards'


class DataloggerFileColumns(models.Model):
    dataloggerfilecolumnid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey('Results', verbose_name="result", db_column='resultid', blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    dataloggerfileid = models.ForeignKey('DataloggerFiles', verbose_name="data logger file",
                                         db_column='dataloggerfileid',
                                         on_delete=models.CASCADE)
    instrumentoutputvariableid = models.ForeignKey('InstrumentOutputVariables',
                                                   verbose_name="instrument output variable",
                                                   db_column='instrumentoutputvariableid',
                                                   on_delete=models.CASCADE)
    columnlabel = models.CharField(verbose_name="column label", max_length=50)
    columndescription = models.CharField(verbose_name="column description",
                                         help_text="To disble ingestion of a column type skip, " +
                                                   "or to specify a column as the date time enter datetime" +
                                                   " if the datetime is an excel format numeric datetime" +
                                                   " enter exceldatetime",
                                         max_length=5000,
                                         blank=True)
    measurementequation = models.CharField(verbose_name="measurement equation", max_length=255,
                                           blank=True)
    scaninterval = models.FloatField(verbose_name="scan interval (time)", blank=True, null=True)
    scanintervalunitsid = models.ForeignKey('Units', verbose_name="scan interval units",
                                            related_name='relatedScanIntervalUnitsid',
                                            db_column='scanintervalunitsid',
                                            blank=True, null=True,
                                            on_delete=models.CASCADE)
    recordinginterval = models.FloatField(verbose_name="recording interval", blank=True, null=True)
    recordingintervalunitsid = models.ForeignKey('Units', verbose_name="recording interval units",
                                                 related_name='relatedRecordingintervalunitsid',
                                                 db_column='recordingintervalunitsid', blank=True,
                                                 null=True,
                                                 on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               verbose_name="aggregation statistic",
                                               db_column='aggregationstatisticcv', blank=True,
                                               null=True,
                                               on_delete=models.CASCADE)

    def __str__(self):
        s = "Label: %s," % self.columnlabel
        s += " Result: %s" % self.resultid
        return s

    class Meta:
        managed = False
        db_table = 'dataloggerfilecolumns'


class DataloggerFiles(models.Model):
    dataloggerfileid = models.AutoField(primary_key=True)
    programid = models.ForeignKey('DataloggerProgramFiles', db_column='programid',
                                  on_delete=models.CASCADE)
    dataloggerfilename = models.CharField(max_length=255, verbose_name="Data logger file name")
    dataloggerfiledescription = models.CharField(max_length=5000, blank=True, verbose_name="Data logger file description")
    dataloggerfilelink = models.CharField(max_length=255, blank=True)
    # dataloggerfilelink = models.FileField(upload_to='dataloggerfiles', verbose_name="Data logger file")  # upload_to='.'

    # def dataloggerfilelinkname(self):
    #    return self.dataloggerfilelink.name

    def __str__(self):
        s = self.dataloggerfilename
        return s

    class Meta:
        managed = False
        db_table = 'dataloggerfiles'


class DataloggerProgramFiles(models.Model):
    programid = models.AutoField(primary_key=True)
    affiliationid = models.ForeignKey(Affiliations, db_column='affiliationid',
                                      on_delete=models.CASCADE)
    programname = models.CharField(max_length=255)
    programdescription = models.CharField(max_length=5000, blank=True)
    programversion = models.CharField(max_length=50, blank=True)
    # programfilelink = models.CharField(max_length=255, blank=True)
    programfilelink = models.FileField(
        upload_to='dataloggerprogramfiles')

    # + '/' + programname.__str__() settings.settings.MEDIA_ROOT upload_to='/upfiles/'

    def __str__(self):
        s = self.programname
        s += " - Version %s" % self.programversion
        return s

    class Meta:
        managed = False
        db_table = 'dataloggerprogramfiles'
        verbose_name = 'data logger program file'


class Equipment(models.Model):
    equipmentid = models.AutoField(primary_key=True)
    equipmentcode = models.CharField(max_length=50)
    equipmentname = models.CharField(max_length=255)
    equipmenttypecv = models.ForeignKey(CvEquipmentType, db_column='equipmenttypecv',
                                        on_delete=models.CASCADE)
    equipmentmodelid = models.ForeignKey('EquipmentModels', db_column='equipmentmodelid',
                                         on_delete=models.CASCADE)
    equipmentserialnumber = models.CharField(max_length=50)
    equipmentownerid = models.ForeignKey('People', db_column='equipmentownerid',
                                         on_delete=models.CASCADE)
    equipmentvendorid = models.ForeignKey('Organizations', db_column='equipmentvendorid',
                                          on_delete=models.CASCADE)
    equipmentpurchasedate = models.DateTimeField()
    equipmentpurchaseordernumber = models.CharField(max_length=50, blank=True)
    equipmentdescription = models.CharField(max_length=5000, blank=True)
    equipmentdocumentationlink = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'equipment'


class EquipmentModels(models.Model):
    equipmentmodelid = models.AutoField(primary_key=True)
    modelmanufacturerid = models.ForeignKey('Organizations', verbose_name="model manufacturer",
                                            db_column='modelmanufacturerid',
                                            on_delete=models.CASCADE)
    modelpartnumber = models.CharField(max_length=50, blank=True, verbose_name="model part number")
    modelname = models.CharField(max_length=255, verbose_name="model name")
    modeldescription = models.CharField(max_length=5000, blank=True, null=True,
                                        verbose_name="model description")
    isinstrument = models.BooleanField(verbose_name="Is this an instrument?")
    modelspecificationsfilelink = models.CharField(max_length=255,
                                                   verbose_name="link to manual for equipment",
                                                   blank=True)
    modellink = models.CharField(max_length=255, verbose_name="link to website for model",
                                 blank=True)

    def __str__(self):
        s = self.modelname
        if self.modelpartnumber:
            s += " - %s" % self.modelpartnumber
        return s

    class Meta:
        managed = False
        db_table = 'equipmentmodels'
        verbose_name = "equipment model"


class EquipmentUsed(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid',
                                 on_delete=models.CASCADE)
    equipmentid = models.ForeignKey(Equipment, db_column='equipmentid',
                                    on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'equipmentused'


class InstrumentOutputVariables(models.Model):
    instrumentoutputvariableid = models.AutoField(primary_key=True)
    modelid = models.ForeignKey(EquipmentModels, verbose_name="equipment model",
                                db_column='modelid',
                                on_delete=models.CASCADE)
    variableid = models.ForeignKey('Variables', verbose_name="variable", db_column='variableid',
                                   on_delete=models.CASCADE)
    instrumentmethodid = models.ForeignKey('Methods', verbose_name="instrument method",
                                           db_column='instrumentmethodid',
                                           on_delete=models.CASCADE)
    instrumentresolution = models.CharField(max_length=255, verbose_name="instrument resolution",
                                            blank=True)
    instrumentaccuracy = models.CharField(max_length=255, verbose_name="instrument accuracy",
                                          blank=True)
    instrumentrawoutputunitsid = models.ForeignKey('Units', related_name='+',
                                                   verbose_name="instrument raw output unit",
                                                   db_column='instrumentrawoutputunitsid',
                                                   on_delete=models.CASCADE)

    def __str__(self):
        s = "%s " % self.modelid
        s += " - %s" % self.variableid
        return s

    class Meta:
        managed = False
        db_table = 'instrumentoutputvariables'
        verbose_name = "instrument output variable"


class MaintenanceActions(models.Model):
    actionid = models.OneToOneField(Actions, db_column='actionid', primary_key=True,
                                 on_delete=models.CASCADE)
    isfactoryservice = models.BooleanField()
    maintenancecode = models.CharField(max_length=50, blank=True)
    maintenancereason = models.CharField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'maintenanceactions'


class RelatedEquipment(models.Model):
    relationid = models.AutoField(primary_key=True)
    equipmentid = models.ForeignKey(Equipment, db_column='equipmentid',
                                    on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedequipmentid = models.ForeignKey(Equipment, related_name='RelatedEquipment',
                                           db_column='relatedequipmentid',
                                           on_delete=models.CASCADE)
    relationshipstartdatetime = models.DateTimeField()
    relationshipstartdatetimeutcoffset = models.IntegerField()
    relationshipenddatetime = models.DateTimeField(blank=True, null=True)
    relationshipenddatetimeutcoffset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relatedequipment'

# </editor-fold>


# <editor-fold desc="ODM2Annotations">

class ActionAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey('Actions', db_column='actionid', on_delete=models.CASCADE)
    annotationid = models.ForeignKey('Annotations', db_column='annotationid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'actionannotations'


class Annotations(models.Model):
    annotationid = models.AutoField(primary_key=True)
    annotationtypecv = models.ForeignKey('CvAnnotationType', db_column='annotationtypecv', on_delete=models.CASCADE)
    annotationcode = models.CharField(max_length=50, blank=True)
    annotationtext = models.CharField(max_length=500)
    annotationdatetime = models.DateTimeField(blank=True, null=True)
    annotationutcoffset = models.IntegerField(blank=True, null=True)
    annotationlink = models.CharField(max_length=255, blank=True)
    annotatorid = models.ForeignKey('People', db_column='annotatorid', blank=True, null=True,
                                    on_delete=models.CASCADE)
    citationid = models.ForeignKey('Citations', db_column='citationid', blank=True, null=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        s = "%s" % self.annotationtext
        return s

    class Meta:
        managed = False
        db_table = 'annotations'


class CategoricalResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('CategoricalResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                 on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = r'categoricalresultvalueannotations'


class EquipmentAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    equipmentid = models.ForeignKey(Equipment, db_column='equipmentid',
                                    on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'equipmentannotations'


class MeasurementResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('MeasurementResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'measurementresultvalueannotations'


class MethodAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    methodid = models.ForeignKey('Methods', db_column='methodid',
                                 on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'methodannotations'


class PointCoverageResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('PointCoverageResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalueannotations'


class ProfileResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('ProfileResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'profileresultvalueannotations'


class RelatedAnnotations(models.Model):
    relationid = models.AutoField(primary_key=True)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedannotationid = models.ForeignKey(Annotations, related_name='RelatedAnnotations',
                                            db_column='relatedannotationid',
                                            on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'relatedannotations'


class ResultAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey('Results', db_column='resultid',
                                  on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)
    begindatetime = models.DateTimeField()
    enddatetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'resultannotations'


class SamplingFeatureAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey('SamplingFeatures', db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    def __str__(self):
        s = self.samplingfeatureid
        if self.annotationid:
            s += " - %s" % self.annotationid
        return s

    class Meta:
        managed = False
        db_table = 'samplingfeatureannotations'


class SectionResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('SectionResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'sectionresultvalueannotations'


class SpectraResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('SpectraResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'spectraresultvalueannotations'


class TimeSeriesResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('TimeSeriesResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalueannotations'


class TrajectoryResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('TrajectoryResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalueannotations'


class TransectResultValueAnnotations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    valueid = models.ForeignKey('TransectResultValues', db_column='valueid',
                                on_delete=models.CASCADE)
    annotationid = models.ForeignKey(Annotations, db_column='annotationid',
                                     on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'transectresultvalueannotations'

# </editor-fold>


# <editor-fold desc="ODM2Provenance">

class AuthorLists(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    citationid = models.ForeignKey('Citations', verbose_name='citation', db_column='citationid',
                                   on_delete=models.CASCADE)
    personid = models.ForeignKey('People', verbose_name='person', db_column='personid', blank=True,
                                 null=True, on_delete=models.CASCADE)
    authororder = models.IntegerField(verbose_name='author order', blank=True, null=True)

    def __str__(self):
        s = "{0} - {1}".format(self.personid, self.authororder)
        return s

    class Meta:
        managed = False
        db_table = 'authorlists'
        verbose_name = 'author list'
        verbose_name_plural = 'author list'


class Citations(models.Model):
    citationid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publicationyear = models.IntegerField(verbose_name='year')
    citationlink = models.CharField(max_length=255, blank=True, verbose_name='Citation Link', )

    def __str__(self):
        s = self.title
        if self.publisher:
            s += " - %s" % self.publisher
        if self.publicationyear:
            s += ", %s" % self.publicationyear
        return s

    class Meta:
        managed = False
        db_table = 'citations'
        ordering = ['title']
        verbose_name = 'citation'


class DatasetCitations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    datasetid = models.ForeignKey('Datasets', verbose_name='dataset', db_column='datasetid',
                                  on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, verbose_name='relationship type',
                                           db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    citationid = models.ForeignKey(Citations, db_column='citationid', verbose_name='citation',
                                   on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'datasetcitations'
        verbose_name = 'dataset citation'


class DerivationEquations(models.Model):
    derivationequationid = models.AutoField(primary_key=True)
    derivationequation = models.CharField(max_length=255, verbose_name='derivation equation')

    def __str__(self):
        s = self.derivationequation
        return s

    class Meta:
        managed = False
        db_table = 'derivationequations'
        verbose_name = 'derivation equation'


class MethodCitations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    methodid = models.ForeignKey('Methods', db_column='methodid', verbose_name='method',
                                 on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           verbose_name='relationship type',
                                           on_delete=models.CASCADE)
    citationid = models.ForeignKey(Citations, db_column='citationid', verbose_name='citation',
                                   on_delete=models.CASCADE)

    def __str__(self):
        s = "%s" % self.methodid
        s += " - %s" % self.citationid
        return s

    class Meta:
        managed = False
        db_table = 'methodcitations'
        verbose_name = 'method citation'


# class RelatedAnnotations(models.Model):...


class RelatedCitations(models.Model):
    relationid = models.AutoField(primary_key=True)
    citationid = models.ForeignKey(Citations, db_column='citationid',
                                   on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedcitationid = models.ForeignKey(Citations, related_name='RelatedCitations',
                                          db_column='relatedcitationid',
                                          on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'relatedcitations'


class RelatedDatasets(models.Model):
    relationid = models.AutoField(primary_key=True)
    datasetid = models.ForeignKey(Datasets, db_column='datasetid',
                                  on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relateddatasetid = models.ForeignKey(Datasets, related_name='relatedDataset',
                                         db_column='relateddatasetid',
                                         on_delete=models.CASCADE)
    versioncode = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'relateddatasets'


class RelatedResults(models.Model):
    relationid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey('Results', db_column='resultid', verbose_name='data result',
                                  on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           verbose_name='relationship type',
                                           on_delete=models.CASCADE)
    relatedresultid = models.ForeignKey('Results', related_name='RelatedResult',
                                        db_column='relatedresultid',
                                        verbose_name='related data result',
                                        on_delete=models.CASCADE)
    versioncode = models.CharField(max_length=50, blank=True, verbose_name='version code')
    relatedresultsequencenumber = models.IntegerField(blank=True, null=True,
                                                      verbose_name='related result sequence number')

    def __str__(self):
        return "%s - %s - %s" % (
            self.resultid, self.relationshiptypecv, self.relatedresultid)

    class Meta:
        managed = False
        db_table = 'relatedresults'
        verbose_name = 'related result'


class ResultDerivationEquations(models.Model):
    resultid = models.OneToOneField('Results', db_column='resultid',
                                    verbose_name='data result', primary_key=True,
                                    on_delete=models.CASCADE)
    derivationequationid = models.ForeignKey(DerivationEquations, db_column='derivationequationid',
                                             on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.resultid, self.derivationequationid)

    class Meta:
        managed = False
        db_table = 'resultderivationequations'
        verbose_name= 'result derivation equation'

# </editor-fold>


# <editor-fold desc="ODM2DataQuality">

class DataQuality(models.Model):
    dataqualityid = models.AutoField(primary_key=True)
    dataqualitytypecv = models.ForeignKey(CvDataQualityType, db_column='dataqualitytypecv',
                                          verbose_name="data quality type",
                                          on_delete=models.CASCADE)
    dataqualitycode = models.CharField(max_length=255, verbose_name="data quality code",
                                       help_text="for an alarm test include the word alarm." +
                                                 " for a hard bounds check include the word bound (if a value" +
                                                 " falls below a lower limit, or exceeds a lower limit the " +
                                                 "value will be set to NaN (not a number). ")
    dataqualityvalue = models.FloatField(blank=True, null=True, verbose_name="data quality value")
    dataqualityvalueunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='dataqualityvalueunitsid',
                                                verbose_name="data quality value units", blank=True,
                                                null=True,
                                                on_delete=models.CASCADE)
    dataqualitydescription = models.CharField(max_length=5000, blank=True,
                                              verbose_name="data quality description")
    dataqualitylink = models.CharField(max_length=255, blank=True, verbose_name="data quality link")

    def __str__(self):
        return "%s - %s - %s" % (
            self.dataqualitycode, self.dataqualityvalue, self.dataqualityvalueunitsid)

    class Meta:
        managed = False
        db_table = 'dataquality'
        verbose_name = 'data quality'
        verbose_name_plural = 'data quality'


class ReferenceMaterials(models.Model):
    referencematerialid = models.AutoField(primary_key=True)
    referencematerialmediumcv = models.ForeignKey(CvMedium,
                                                  db_column='referencematerialmediumcv',
                                                  on_delete=models.CASCADE)
    referencematerialorganizationid = models.ForeignKey(Organizations,
                                                        db_column='referencematerialorganizationid',
                                                        on_delete=models.CASCADE)
    referencematerialcode = models.CharField(max_length=50)
    referencemateriallotcode = models.CharField(max_length=255, blank=True)
    referencematerialpurchasedate = models.DateTimeField(blank=True, null=True)
    referencematerialexpirationdate = models.DateTimeField(blank=True, null=True)
    referencematerialcertificatelink = models.CharField(max_length=255, blank=True)
    samplingfeatureid = models.ForeignKey('SamplingFeatures', db_column='samplingfeatureid',
                                          blank=True, null=True,
                                          on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'referencematerials'


class ReferenceMaterialValues(models.Model):
    referencematerialvalueid = models.AutoField(primary_key=True)
    referencematerialid = models.ForeignKey(ReferenceMaterials, db_column='referencematerialid',
                                            on_delete=models.CASCADE)
    referencematerialvalue = models.FloatField()
    referencematerialaccuracy = models.FloatField(blank=True, null=True)
    variableid = models.ForeignKey('Variables', db_column='variableid',
                                    on_delete=models.CASCADE)
    unitsid = models.ForeignKey('Units', related_name='+', db_column='unitsid',
                                 on_delete=models.CASCADE)
    citationid = models.ForeignKey(Citations, db_column='citationid',
                                   on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'referencematerialvalues'


class ResultNormalizationValues(models.Model):
    resultid = models.OneToOneField('Results', db_column='resultid', primary_key=True,
                                     on_delete=models.CASCADE)
    normalizedbyreferencematerialvalueid = models.ForeignKey(
        ReferenceMaterialValues,
        db_column='normalizedbyreferencematerialvalueid',
        on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'resultnormalizationvalues'


class ResultsDataQuality(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(Results, db_column='resultid', verbose_name='result',
                                 on_delete=models.CASCADE)
    dataqualityid = models.ForeignKey(DataQuality, db_column='dataqualityid',
                                      verbose_name='data quality',
                                      on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.resultid, self.dataqualityid)

    class Meta:
        managed = False
        db_table = 'resultsdataquality'
        verbose_name = 'results data quality'
        verbose_name_plural = 'results data quality'

# </editor-fold>


# <editor-fold desc="ODM2ExtensionProperties">

class ActionExtensionPropertyValues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey('Actions', db_column='actionid', on_delete=models.CASCADE)
    propertyid = models.ForeignKey('ExtensionProperties', db_column='propertyid', on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actionextensionpropertyvalues'


class Citationextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    citationid = models.ForeignKey('Citations', db_column='citationid',
                                   on_delete=models.CASCADE)
    propertyid = models.ForeignKey('ExtensionProperties', db_column='propertyid',
                                   on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        s = "%s - %s - %s" % (self.citationid, self.propertyid, self.propertyvalue)
        return s

    class Meta:
        managed = False
        db_table = 'citationextensionpropertyvalues'
        verbose_name = 'citation extension property'
        verbose_name_plural = 'citation extension properties'


class ExtensionProperties(models.Model):
    propertyid = models.AutoField(primary_key=True)
    propertyname = models.CharField(max_length=255, verbose_name="property name")
    propertydescription = models.CharField(max_length=5000, blank=True,
                                           verbose_name="property description")
    propertydatatypecv = models.ForeignKey(CvPropertyDataType, db_column='propertydatatypecv',
                                           verbose_name="property data type",
                                           on_delete=models.CASCADE)
    propertyunitsid = models.ForeignKey('Units', db_column='propertyunitsid', blank=True, null=True,
                                        verbose_name="units for property",
                                        on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.propertyname, self.propertydescription)

    class Meta:
        managed = False
        db_table = 'extensionproperties'
        verbose_name = 'extension property'
        verbose_name_plural = 'extension properties'


class MethodExtensionPropertyValues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    methodid = models.ForeignKey('Methods', db_column='methodid',
                                 on_delete=models.CASCADE)
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid',
                                   on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'methodextensionpropertyvalues'


class ResultExtensionPropertyValues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey('Results', db_column='resultid',
                                  on_delete=models.CASCADE)
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid',
                                   on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s: value %s" % (self.resultid, self.propertyid, self.propertyvalue)

    class Meta:
        managed = False
        db_table = 'resultextensionpropertyvalues'


class SamplingFeatureExtensionPropertyValues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey('SamplingFeatures', db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid',
                                   on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255)

    def __str__(self):
        s = self.samplingfeatureid
        if self.propertyvalue:
            s += " - %s - %s%s" % (
            self.propertyid.propertyname, self.propertyvalue, self.propertyid.propertyunitsid.unitsabbreviation)
        return s

    class Meta:
        managed = False
        db_table = 'samplingfeatureextensionpropertyvalues'


class VariableExtensionPropertyValues(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    variableid = models.ForeignKey('Variables', db_column='variableid',
                                    on_delete=models.CASCADE)
    propertyid = models.ForeignKey(ExtensionProperties, db_column='propertyid',
                                   on_delete=models.CASCADE)
    propertyvalue = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'variableextensionpropertyvalues'

# </editor-fold>


# <editor-fold desc="ODM2ExternalIdentifiers">

class CitationExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    citationid = models.ForeignKey('Citations', db_column='citationid',
                                   on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey('ExternalIdentifierSystems',
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    citationexternalidentifier = models.CharField(max_length=255,
                                                  db_column="citationexternalidentifier")
    citationexternalidentifieruri = models.CharField(max_length=255, blank=True,
                                                     db_column="citationexternalidentifieruri")

    def __str__(self):
        s = "{0} - {1}".format(self.externalidentifiersystemid, self.citationexternalidentifier)
        return s

    class Meta:
        managed = False
        db_table = 'citationexternalidentifiers'
        verbose_name = 'citationexternalidentifier'


class ExternalIdentifierSystems(models.Model):
    externalidentifiersystemid = models.AutoField(primary_key=True)
    externalidentifiersystemname = models.CharField(max_length=255)
    identifiersystemorganizationid = models.ForeignKey('Organizations',
                                                       db_column='identifiersystemorganizationid',
                                                       on_delete=models.CASCADE)
    externalidentifiersystemdescription = models.CharField(max_length=5000, blank=True)
    externalidentifiersystemurl = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.externalidentifiersystemname

    class Meta:
        managed = False
        db_table = 'externalidentifiersystems'


class MethodExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    methodid = models.ForeignKey('Methods', db_column='methodid',
                                 on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    methodexternalidentifier = models.CharField(max_length=255)
    methodexternalidentifieruri = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'methodexternalidentifiers'


class PersonExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    personid = models.ForeignKey(People, db_column='personid',
                                 on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    personexternalidentifier = models.CharField(max_length=255)
    personexternalidentifieruri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        s = "%s - %s - %s - %s" % (
            self.personid, self.externalidentifiersystemid, self.personexternalidentifier,
            self.personexternalidentifieruri)
        return s

    class Meta:
        managed = False
        db_table = 'personexternalidentifiers'
        verbose_name_plural = 'ORCID (Person Unique Identifier)'


class ReferenceMaterialExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    referencematerialid = models.ForeignKey('ReferenceMaterials', db_column='referencematerialid',
                                            on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    referencematerialexternalidentifier = models.CharField(max_length=255)
    referencematerialexternalidentifieruri = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'referencematerialexternalidentifiers'


class SamplingFeatureExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey('SamplingFeatures', db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    samplingfeatureexternalidentifier = models.CharField(max_length=255)
    samplingfeatureexternalidentifieruri = models.CharField(max_length=255, blank=True)

    def __str__(self):
        s = "%s - %s - %s - %s" % (
            self.samplingfeatureid, self.externalidentifiersystemid,
            self.samplingfeatureexternalidentifier,
            self.samplingfeatureexternalidentifieruri)
        return s

    class Meta:
        managed = False
        db_table = 'samplingfeatureexternalidentifiers'


class SpatialReferenceExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    spatialreferenceid = models.ForeignKey('SpatialReferences', db_column='spatialreferenceid',
                                           on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    spatialreferenceexternalidentifier = models.CharField(max_length=255)
    spatialreferenceexternalidentifieruri = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'spatialreferenceexternalidentifiers'


class TaxonomicClassifierExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifiers',
                                              db_column='taxonomicclassifierid',
                                              on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    taxonomicclassifierexternalidentifier = models.CharField(max_length=255)
    taxonomicclassifierexternalidentifieruri = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'taxonomicclassifierexternalidentifiers'

    # I needed to add a sequence and set it as the default for the primary
    # key to make the Taxonomic Classifiers class work.
    # This is the SQL:

    # CREATE SEQUENCE odm2.taxonomicclassifiers_taxonomicclassifiersid_seq
    #   INCREMENT 1
    #   MINVALUE 2
    #   MAXVALUE 9223372036854775807
    #   START 3
    #   CACHE 1;
    # ALTER TABLE odm2.taxonomicclassifiers_taxonomicclassifiersid_seq
    #   OWNER TO postgres;

    # ALTER TABLE odm2.taxonomicclassifiers
    #  ALTER COLUMN taxonomicclassifierid SET DEFAULT nextval
    # ('odm2.taxonomicclassifiers_taxonomicclassifiersid_seq'::regclass);


class VariableExternalIdentifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    variableid = models.ForeignKey('Variables', db_column='variableid',
                                    on_delete=models.CASCADE)
    externalidentifiersystemid = models.ForeignKey(ExternalIdentifierSystems,
                                                   db_column='externalidentifiersystemid',
                                                   on_delete=models.CASCADE)
    variableexternalidentifier = models.CharField(max_length=255)
    variableexternalidentifieruri = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'variableexternalidentifiers'

# </editor-fold>


# <editor-fold desc="ODM2LabAnalyses">

class ActionDirectives(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey('Actions', db_column='actionid', on_delete=models.CASCADE)
    directiveid = models.ForeignKey('Directives', db_column='directiveid', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'actiondirectives'


class Directives(models.Model):
    directiveid = models.AutoField(primary_key=True)
    directivetypecv = models.ForeignKey(CvDirectiveType, db_column='directivetypecv',
                                        on_delete=models.CASCADE)
    directivedescription = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'directives'


class SpecimenBatchPostions(models.Model):
    featureactionid = models.OneToOneField(FeatureActions, db_column='featureactionid',
                                           primary_key=True,
                                           on_delete=models.CASCADE)
    batchpositionnumber = models.IntegerField()
    batchpositionlabel = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'specimenbatchpostions'

# </editor-fold>


# <editor-fold desc="ODM2SamplingFeatures">

class RelatedFeatures(models.Model):
    relationid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey('SamplingFeatures', verbose_name="first feature",
                                          db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, verbose_name="relationship type",
                                           db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedfeatureid = models.ForeignKey('SamplingFeatures', verbose_name="second feature",
                                         related_name='RelatedFeatures',
                                         db_column='relatedfeatureid',
                                         on_delete=models.CASCADE)
    spatialoffsetid = models.ForeignKey('SpatialOffsets', verbose_name="spatial offset",
                                        db_column='spatialoffsetid',
                                        blank=True, null=True,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %s" % (
            self.samplingfeatureid, self.relationshiptypecv, self.relatedfeatureid)

    class Meta:
        managed = False
        db_table = 'relatedfeatures'
        verbose_name = 'relate two feature'


class Sites(models.Model):
    samplingfeatureid = models.OneToOneField(SamplingFeatures, db_column='samplingfeatureid',
                                             primary_key=True, verbose_name='sampling feature',
                                             on_delete=models.CASCADE)
    sitetypecv = models.ForeignKey(CvSiteType, db_column='sitetypecv',
                                   on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    spatialreferenceid = models.ForeignKey('SpatialReferences', verbose_name='spatial reference id',
                                           db_column='spatialreferenceid',
                                           on_delete=models.CASCADE)

    def __str__(self):
        s = self.samplingfeatureid
        s += " - %s" % self.sitetypecv
        return s

    class Meta:
        managed = False
        verbose_name = 'Site'
        db_table = 'sites'


class SpatialOffsets(models.Model):
    spatialoffsetid = models.AutoField(primary_key=True)
    spatialoffsettypecv = models.ForeignKey(CvSpatialOffsetType, db_column='spatialoffsettypecv',
                                            on_delete=models.CASCADE)
    offset1value = models.FloatField()
    offset1unitid = models.ForeignKey('Units', related_name='+', db_column='offset1unitid',
                                       on_delete=models.CASCADE)
    offset2value = models.FloatField(blank=True, null=True)
    offset2unitid = models.ForeignKey('Units', related_name='+', db_column='offset2unitid',
                                      blank=True, null=True,
                                      on_delete=models.CASCADE)
    offset3value = models.FloatField(blank=True, null=True)
    offset3unitid = models.ForeignKey('Units', related_name='+', db_column='offset3unitid',
                                      blank=True, null=True,
                                      on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'spatialoffsets'


class SpatialReferences(models.Model):
    spatialreferenceid = models.AutoField(primary_key=True, verbose_name='spatial reference id')
    srscode = models.CharField(max_length=50, blank=True, verbose_name='spatial reference code')
    srsname = models.CharField(max_length=255, verbose_name='spatial reference name')
    srsdescription = models.CharField(max_length=5000, blank=True,
                                      verbose_name='spatial reference description')
    srslink = models.CharField(max_length=255, blank=True, verbose_name='spatial reference link')

    def __str__(self):
        s = ''
        if self.srscode:
            s = "{} - ".format(self.srscode)
        s += "%s" % self.srsname
        return s

    class Meta:
        managed = False
        verbose_name = 'Spatial reference'
        db_table = 'spatialreferences'


class Specimens(models.Model):
    samplingfeatureid = models.OneToOneField(SamplingFeatures, db_column='samplingfeatureid',
                                             primary_key=True,
                                             on_delete=models.CASCADE)
    specimentypecv = models.ForeignKey(CvSpecimenType, db_column='specimentypecv',
                                       on_delete=models.CASCADE)
    specimenmediumcv = models.ForeignKey(CvSpecimenMedium, db_column='specimenmediumcv',
                                         on_delete=models.CASCADE)
    isfieldspecimen = models.BooleanField()

    def __unicode__(self):
        return u'{spectypecv} - {specmedcv}'.format(spectypecv=self.specimentypecv,
                                                    specmedcv=self.specimenmediumcv)

    class Meta:
        managed = False
        db_table = 'specimens'
        verbose_name = 'Specimen'


class SpecimenTaxonomicClassifiers(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    samplingfeatureid = models.ForeignKey(Specimens, db_column='samplingfeatureid',
                                          on_delete=models.CASCADE)
    taxonomicclassifierid = models.ForeignKey('TaxonomicClassifiers',
                                              db_column='taxonomicclassifierid',
                                              on_delete=models.CASCADE)
    citationid = models.ForeignKey(Citations, db_column='citationid', blank=True, null=True,
                                   on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'specimentaxonomicclassifiers'

# </editor-fold>


# <editor-fold desc="ODM2Results">

class CategoricalResults(models.Model):
    resultid = models.OneToOneField('Results', db_column='resultid', primary_key=True,
                                 on_delete=models.CASCADE)
    xlocation = models.FloatField(blank=True, null=True)
    xlocationunitsid = models.IntegerField(blank=True, null=True)
    ylocation = models.FloatField(blank=True, null=True)
    ylocationunitsid = models.IntegerField(blank=True, null=True)
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.IntegerField(blank=True, null=True)
    spatialreferenceid = models.ForeignKey('SpatialReferences', db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey('CvQualityCode', db_column='qualitycodecv',
                                      on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'categoricalresults'


class CategoricalResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(CategoricalResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.CharField(max_length=255)
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoricalresultvalues'


class MeasurementResults(models.Model):
    resultid = models.OneToOneField('Results', verbose_name="Result Series", db_column='resultid',
                                    primary_key=True,
                                    on_delete=models.CASCADE)
    xlocation = models.FloatField(verbose_name="x location", blank=True, null=True)
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='relatedXlocationUnits',
                                         db_column='xlocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    ylocation = models.FloatField(blank=True, verbose_name="y location", null=True)
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='relatedYlocationUnits',
                                         db_column='ylocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    zlocation = models.FloatField(blank=True, verbose_name="z location", null=True)
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='relatedZlocationUnits',
                                         db_column='zlocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey('SpatialReferences', verbose_name="spatial reference",
                                           db_column='spatialreferenceid', blank=True, null=True,
                                           on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, verbose_name="censor code",
                                     db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, verbose_name="quality code",
                                      db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               verbose_name="aggregation statistic",
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField(verbose_name="time aggregation interval")
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       verbose_name="time aggregation " +
                                                                    "interval unit",
                                                       related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    def __str__(self):
        s = "%s" % self.resultid
        s += ", %s" % self.qualitycodecv
        return s

    class Meta:
        managed = False
        db_table = 'measurementresults'
        ordering = ['censorcodecv', 'resultid']
        verbose_name = 'measurement result'


class MeasurementResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(MeasurementResults, verbose_name='Result Series',
                                 db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField(verbose_name='data value')
    valuedatetime = models.DateTimeField(verbose_name='value date time')
    valuedatetimeutcoffset = models.IntegerField(verbose_name='value date time UTC offset',
                                                 default=4)

    def __str__(self):
        s = "%s" % self.resultid
        s += " - %s" % self.datavalue
        s += " - %s" % self.valuedatetime
        return s

    class Meta:
        managed = False
        db_table = 'measurementresultvalues'
        verbose_name = 'measurement result value'


class PointCoverageResults(models.Model):
    resultid = models.OneToOneField('Results', db_column='resultid', primary_key=True,
                                     on_delete=models.CASCADE)
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey('SpatialReferences', db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedxspacing = models.FloatField(blank=True, null=True)
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='intendedxspacingunitsid',
                                                blank=True, null=True,
                                                on_delete=models.CASCADE)
    intendedyspacing = models.FloatField(blank=True, null=True)
    intendedyspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='intendedyspacingunitsid',
                                                blank=True, null=True,
                                                on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pointcoverageresults'


class PointCoverageResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(PointCoverageResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.BigIntegerField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()
    xlocation = models.FloatField()
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                          on_delete=models.CASCADE)
    ylocation = models.FloatField()
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                          on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'pointcoverageresultvalues'


class ProfileResults(models.Model):
    resultid = models.OneToOneField('Results', verbose_name='result', db_column='resultid',
                                    primary_key=True,
                                    on_delete=models.CASCADE)
    xlocation = models.FloatField(blank=True, verbose_name='x location', null=True)
    xlocationunitsid = models.ForeignKey('Units', verbose_name='x location units', related_name='+',
                                         db_column='xlocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    ylocation = models.FloatField(blank=True, verbose_name='y location', null=True)
    ylocationunitsid = models.ForeignKey('Units', related_name='+', verbose_name='y location units',
                                         db_column='ylocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey('SpatialReferences', verbose_name='spatial reference',
                                           db_column='spatialreferenceid', blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedzspacing = models.FloatField(blank=True, verbose_name='intended depth', null=True)
    intendedzspacingunitsid = models.ForeignKey('Units', verbose_name='intended depth units',
                                                related_name='+',
                                                db_column='intendedzspacingunitsid', blank=True,
                                                null=True,
                                                on_delete=models.CASCADE)
    intendedtimespacing = models.FloatField(blank=True, null=True,
                                            verbose_name='intended time spacing')
    intendedtimespacingunitsid = models.ForeignKey('Units',
                                                   verbose_name='intended time spacing unit',
                                                   related_name='+',
                                                   db_column='intendedtimespacingunitsid',
                                                   blank=True, null=True,
                                                   on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               verbose_name='aggregation statistic',
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    def __str__(self):
        s = self.resultid
        if self.xlocation:
            s += "- %s" % self.xlocation
        if self.xlocationunitsid:
            s += ", %s" % self.xlocationunitsid
        if self.ylocation:
            s += "- %s" % self.ylocation
        if self.ylocationunitsid:
            s += ", %s" % self.ylocationunitsid
        if self.intendedzspacing:
            s += "- %s" % self.intendedzspacing
        if self.intendedzspacingunitsid:
            s += ", %s" % self.intendedzspacingunitsid
        return s

    class Meta:
        managed = False
        db_table = 'profileresults'
        verbose_name = 'profile result'


class ProfileResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(ProfileResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField(verbose_name='data value')
    valuedatetime = models.DateTimeField(verbose_name='value date and time', blank=True, null=True)
    valuedatetimeutcoffset = models.IntegerField(verbose_name='value date and time UTC offset',
                                                 blank=True, null=True)
    zlocation = models.FloatField(verbose_name='z location', blank=True, null=True)
    zaggregationinterval = models.FloatField(verbose_name='z aggregation interval', blank=True,
                                             null=True)
    zlocationunitsid = models.ForeignKey('Units', verbose_name='z location unit', related_name='+',
                                         db_column='zlocationunitsid', blank=True, null=True,
                                         on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, verbose_name='censor code',
                                     db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, verbose_name='quality code',
                                      db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField(verbose_name='time aggregation interval',
                                                blank=True, null=True)
    timeaggregationintervalunitsid = models.ForeignKey('Units',
                                                       verbose_name='time aggregation ' +
                                                                    'interval unit',
                                                       related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       blank=True, null=True,
                                                       on_delete=models.CASCADE)

    def __str__(self):
        s = "%s " % self.resultid
        s += ", %s" % self.datavalue
        s += ", %s" % self.zlocation
        # s += ", %s" % (self.zaggregationinterval)
        s += ", %s" % self.zlocationunitsid
        return s

    class Meta:
        managed = False
        db_table = 'profileresultvalues'
        verbose_name = 'profile result value'


class SectionResults(models.Model):
    resultid = models.OneToOneField(Results, db_column='resultid', primary_key=True,
                                    on_delete=models.CASCADE)
    ylocation = models.FloatField(blank=True, null=True)
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey('SpatialReferences', db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedxspacing = models.FloatField(blank=True, null=True)
    intendedxspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='intendedxspacingunitsid',
                                                blank=True, null=True,
                                                on_delete=models.CASCADE)
    intendedzspacing = models.FloatField(blank=True, null=True)
    intendedzspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='intendedzspacingunitsid',
                                                blank=True, null=True,
                                                on_delete=models.CASCADE)
    intendedtimespacing = models.FloatField(blank=True, null=True)
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='+',
                                                   db_column='intendedtimespacingunitsid',
                                                   blank=True, null=True,
                                                   on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'sectionresults'


class SectionResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(SectionResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField()
    valuedatetime = models.BigIntegerField()
    valuedatetimeutcoffset = models.BigIntegerField()
    xlocation = models.FloatField()
    xaggregationinterval = models.FloatField()
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                          on_delete=models.CASCADE)
    zlocation = models.BigIntegerField()
    zaggregationinterval = models.FloatField()
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                          on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'sectionresultvalues'


class SpectraResults(models.Model):
    resultid = models.OneToOneField(Results, db_column='resultid', primary_key=True,
                                    on_delete=models.CASCADE)
    xlocation = models.FloatField(blank=True, null=True)
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    ylocation = models.FloatField(blank=True, null=True)
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(SpatialReferences, db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedwavelengthspacing = models.FloatField(blank=True, null=True)
    intendedwavelengthspacingunitsid = models.ForeignKey('Units',
                                                         related_name='+',
                                                         db_column='intendedwavelengthspacingunitsid',
                                                         blank=True,
                                                         null=True,
                                                         on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'spectraresults'


class SpectraResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(SpectraResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()
    excitationwavelength = models.FloatField()
    emissionwavelength = models.FloatField()
    wavelengthunitsid = models.ForeignKey('Units', related_name='+', db_column='wavelengthunitsid',
                                           on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'spectraresultvalues'


class TimeSeriesResults(models.Model):
    resultid = models.OneToOneField(Results, verbose_name="Result Series", db_column='resultid',
                                    primary_key=True,
                                    on_delete=models.CASCADE)
    xlocation = models.FloatField(blank=True, null=True, verbose_name="x location")
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                         blank=True, null=True, verbose_name="x location units",
                                         on_delete=models.CASCADE)
    ylocation = models.FloatField(blank=True, null=True, verbose_name="y location")
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                         verbose_name="y location units", blank=True, null=True,
                                         on_delete=models.CASCADE)
    zlocation = models.FloatField(blank=True, null=True, verbose_name="z location")
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                         verbose_name="z location units", blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(SpatialReferences, db_column='spatialreferenceid',
                                           verbose_name="spatial reference",
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedtimespacing = models.FloatField(blank=True, null=True, verbose_name="Intended time spacing",
                                            help_text="time between measurements")
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='+',
                                                   help_text="Units of time between measurements. This defines the time"
                                                             " series 1 hour, or 15 minutes for example.",
                                                   verbose_name="Time Units",
                                                   db_column='intendedtimespacingunitsid',
                                                   blank=True, null=True,
                                                   on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    def __str__(self):
        s = "%s " % self.resultid
        s += ", %s" % self.intendedtimespacing
        s += ", %s" % self.intendedtimespacingunitsid
        return s

    class Meta:
        managed = False
        db_table = 'timeseriesresults'
        ordering = ['resultid']
        verbose_name = 'time series result'


class TimeSeriesResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(TimeSeriesResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField(verbose_name="Time Interval")
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='+',
                                                       verbose_name="Time Units",
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    def __str__(self):
        s = "%s " % self.resultid
        s += "- %s" % self.datavalue
        s += "- %s" % self.qualitycodecv
        s += "- %s" % self.valuedatetime
        return s

    class Meta:
        managed = False
        db_table = 'timeseriesresultvalues'
        verbose_name = 'time series result value'


class TrajectoryResults(models.Model):
    resultid = models.OneToOneField(Results, db_column='resultid', primary_key=True,
                                    on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(SpatialReferences, db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedtrajectoryspacing = models.FloatField(blank=True, null=True)
    intendedtrajectoryspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                         db_column='intendedtrajec'
                                                                   'toryspacingunitsid',
                                                         blank=True,
                                                         null=True,
                                                         on_delete=models.CASCADE)
    intendedtimespacing = models.FloatField(blank=True, null=True)
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='+',
                                                   db_column='intendedtimespacingunitsid',
                                                   blank=True, null=True,
                                                   on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'trajectoryresults'


class TrajectoryResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(TrajectoryResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.IntegerField()
    xlocation = models.FloatField()
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                 on_delete=models.CASCADE)
    ylocation = models.FloatField()
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                 on_delete=models.CASCADE)
    zlocation = models.FloatField()
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                 on_delete=models.CASCADE)
    trajectorydistance = models.FloatField()
    trajectorydistanceaggregationinterval = models.FloatField()
    trajectorydistanceunitsid = models.ForeignKey('Units', related_name='+',
                                                  db_column='trajectorydistanceunitsid',
                                                  on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'trajectoryresultvalues'


class TransectResults(models.Model):
    resultid = models.OneToOneField(Results, db_column='resultid', primary_key=True,
                                    on_delete=models.CASCADE)
    zlocation = models.FloatField(blank=True, null=True)
    zlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='zlocationunitsid',
                                         blank=True, null=True,
                                         on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(SpatialReferences, db_column='spatialreferenceid',
                                           blank=True, null=True,
                                           on_delete=models.CASCADE)
    intendedtransectspacing = models.FloatField(blank=True, null=True)
    intendedtransectspacingunitsid = models.ForeignKey('Units', related_name='+',
                                                       db_column='intendedtransectspacingunitsid',
                                                       blank=True,
                                                       null=True,
                                                       on_delete=models.CASCADE)
    intendedtimespacing = models.FloatField(blank=True, null=True)
    intendedtimespacingunitsid = models.ForeignKey('Units', related_name='+',
                                                   db_column='intendedtimespacingunitsid',
                                                   blank=True, null=True,
                                                   on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'transectresults'


class TransectResultValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    resultid = models.ForeignKey(TransectResults, db_column='resultid',
                                 on_delete=models.CASCADE)
    datavalue = models.FloatField()
    valuedatetime = models.DateTimeField()
    valuedatetimeutcoffset = models.DateTimeField()
    xlocation = models.FloatField()
    xlocationunitsid = models.ForeignKey('Units', related_name='+', db_column='xlocationunitsid',
                                 on_delete=models.CASCADE)
    ylocation = models.FloatField()
    ylocationunitsid = models.ForeignKey('Units', related_name='+', db_column='ylocationunitsid',
                                 on_delete=models.CASCADE)
    transectdistance = models.FloatField()
    transectdistanceaggregationinterval = models.FloatField()
    transectdistanceunitsid = models.ForeignKey('Units', related_name='+',
                                                db_column='transectdistanceunitsid',
                                                on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorCode, db_column='censorcodecv',
                                     on_delete=models.CASCADE)
    qualitycodecv = models.ForeignKey(CvQualityCode, db_column='qualitycodecv',
                                      on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationStatistic,
                                               db_column='aggregationstatisticcv',
                                               on_delete=models.CASCADE)
    timeaggregationinterval = models.FloatField()
    timeaggregationintervalunitsid = models.ForeignKey('Units', related_name='+',
                                                       db_column='timeaggregationintervalunitsid',
                                                       on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'transectresultvalues'

# </editor-fold>


# <editor-fold desc="ODM2Simulation">

class ModelAffiliations(models.Model):
    bridgeid = models.AutoField(primary_key=True)
    modelid = models.ForeignKey('Models', db_column='modelid',
                                 on_delete=models.CASCADE)
    affiliationid = models.ForeignKey(Affiliations, db_column='affiliationid',
                                      on_delete=models.CASCADE)
    isprimary = models.BooleanField()
    roledescription = models.CharField(max_length=5000, blank=True)

    class Meta:
        managed = False
        db_table = 'modelaffiliations'


class Models(models.Model):
    modelid = models.AutoField(primary_key=True)
    modelcode = models.CharField(max_length=50)
    modelname = models.CharField(max_length=255)
    modeldescription = models.CharField(max_length=5000, blank=True)
    version = models.CharField(max_length=255, blank=True)
    modellink = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'models'


class RelatedModels(models.Model):
    relatedid = models.AutoField(primary_key=True)
    modelid = models.ForeignKey(Models, db_column='modelid',
                                on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshipType, db_column='relationshiptypecv',
                                           on_delete=models.CASCADE)
    relatedmodelid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'relatedmodels'


class Simulations(models.Model):
    simulationid = models.AutoField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid',
                                 on_delete=models.CASCADE)
    simulationname = models.CharField(max_length=255)
    simulationdescription = models.CharField(max_length=5000, blank=True)
    simulationstartdatetime = models.DateTimeField()
    simulationstartdatetimeutcoffset = models.IntegerField()
    simulationenddatetime = models.DateTimeField()
    simulationenddatetimeutcoffset = models.IntegerField()
    timestepvalue = models.FloatField()
    timestepunitsid = models.IntegerField()
    inputdatasetid = models.IntegerField(blank=True, null=True)
    modelid = models.ForeignKey(Models, db_column='modelid',
                                on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'simulations'

# </editor-fold>
