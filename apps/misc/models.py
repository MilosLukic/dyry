from django.db import models

# Create your models here.
class Metric(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255)

    discrete = models.BooleanField(default=False)
    units = models.CharField(max_length=255)