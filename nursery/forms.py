from django import forms
from .models import Plants

class AddPlantsForm(forms.ModelForm): 

    # def __init__(self, *args, **kwargs):

    #     super(AddPlantsForm, self).__init__(*args, **kwargs)
    #     self.fields['manager'].widget.attrs['disabled'] = True
    
    class Meta:
        model = Plants
        fields = ('plant_name','plant_desc','plant_price')
    