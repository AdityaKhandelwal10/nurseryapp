from django import forms
from .models import Plants

class AddPlantsForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = '__all__' 