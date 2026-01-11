from django import forms
from .models import LaptopModel

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = LaptopModel
        fields = '__all__'