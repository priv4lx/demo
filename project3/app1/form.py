from . models import Details
from django import forms

class Detailsform(forms.ModelForm):
    class Meta:
        model = Details
        fields = '__all__'