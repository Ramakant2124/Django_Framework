from .models import CourseModel
from django import forms

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
