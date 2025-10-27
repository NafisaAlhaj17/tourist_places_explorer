from django import forms
from .models import Place

class PlaceSearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False)
    city = forms.CharField(label='City', required=False)
    category = forms.CharField(label='Category', required=False)
