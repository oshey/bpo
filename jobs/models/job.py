from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import CASCADE
from django.utils.translation import ugettext_lazy as _

from bpo.settings import AUTH_USER_MODEL


class Job(models.Model):
    EMP_TERMS = (('ft', 'Full-Time'), ('pt', 'Part-Time'), ('tm', 'Temporary'), ('ct', 'Contract'))

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE, related_name='user')
    applicants = models.ManyToManyField(AUTH_USER_MODEL, through='application')
    emp = models.CharField(_('Employer'), max_length=100)
    title = models.CharField(_('Title'), max_length=150)
    ref_code = models.CharField(_('Ref. Code'), max_length=150)
    est_salary = models.PositiveIntegerField(_('Est. Salary'), default=0)
    num_pos = models.PositiveIntegerField(_('Number of Positions'), default=100)
    terms = models.CharField(_('Emp. Terms'), choices=EMP_TERMS, default='ft', max_length=2)
    summary = models.CharField(max_length=255)
    # content = models.TextField()
    content = RichTextField(config_name='basic_ckeditor')
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.title
