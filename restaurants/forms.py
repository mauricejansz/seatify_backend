from django import forms
from .models import Cuisine

class CuisineForm(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = ['name', 'image', 'keyword']