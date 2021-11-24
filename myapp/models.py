from django.db import models


# Create your models here.

class Data20201021(models.Model):
    about = models.CharField(max_length=255, null=True)
    title = models.ArrayField(null=True)
    description = models.ArrayField(null=True)
    issued = models.CharField(max_length=255, null=True)
    theme = models.ArrayField( null=True)
    spatial = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    keyword = models.ArrayField(null=True)
    distributions = models.ArrayField(max_length=255, null=True)
    correlations = models.CharField(max_length=255, null=True)
    dateofDocument = models.DateField(max_length=255)
    dateofPublication = models.DateField(max_length=255)
    idLocal = models.CharField(max_length=255, null=True)
    number = models.CharField(max_length=255, null=True)
    passed_by = models.CharField(max_length=255, null=True)
    entry_into_force = models.CharField(max_length=255, null=True)
    date_no_longer_in_force = models.CharField(max_length=255, null=True)
    typeofDocument = models.CharField(max_length=255, null=True)
    metadata = models.CharField(max_length=255, null=True)
    events = models.CharField(max_length=255, null=True)
    ActIdentifier = models.CharField(max_length=255, null=True)
    mlextra = models.CharField(max_length=255, null=True)
    body= models.JSONField(null=True)

    def __init__(self):
        return self.name
