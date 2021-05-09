from django import forms

from jobs.models import Job


class JobModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = {'class': 'form-control'}

        self.fields['emp'].widget.attrs.update(classes)
        self.fields['title'].widget.attrs.update(classes)
        self.fields['ref_code'].widget.attrs.update(classes)
        self.fields['est_salary'].widget.attrs.update(classes)
        self.fields['num_pos'].widget.attrs.update(classes)
        self.fields['terms'].widget.attrs.update(classes)
        self.fields['summary'].widget.attrs.update(classes)
        self.fields['content'].widget.attrs.update(classes)
        # self.fields['publish'].widget.attrs.update(classes)

    class Meta:
        model = Job

        fields = ['emp', 'title', 'ref_code', 'est_salary', 'num_pos', 'terms', 'summary', 'content', 'publish']


