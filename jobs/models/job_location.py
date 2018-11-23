from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField

from jobs.models.job import Job


class JobLocation(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='job_location')
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(_('State/Parish'), max_length=100)
    country = CountryField(default='jm')
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
