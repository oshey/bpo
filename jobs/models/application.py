from django.db import models
from django.db.models import CASCADE

from bpo.settings import AUTH_USER_MODEL
from jobs.models.job import Job


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=CASCADE, related_name='job')
    applicant = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE, related_name='applicant')
    processed = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
