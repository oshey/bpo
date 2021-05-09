from django import forms

from jobs.models import JobLocation


class JobLocationModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = {'class': 'form-control'}

        self.fields['address_1'].widget.attrs.update(classes)
        self.fields['address_2'].widget.attrs.update(classes)
        self.fields['city'].widget.attrs.update(classes)
        self.fields['state'].widget.attrs.update(classes)
        self.fields['country'].widget.attrs.update(classes)

    class Meta:
        model = JobLocation

        fields = ['address_1', 'address_2', 'city', 'state', 'country']
