from django import forms
from .models import BuyerProfile,User,ManagerProfile
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2','category')

    # def save(self, commit = True):
    #     user = super(NewUserForm,self).save(commit=False)
    #     user.email= self.cleaned_data.get("email")
    #     user.category = self.cleaned_data.get("category")
    #     if commit:
    #         user.save()
    #         return user


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username','email')


class BuyerForm(forms.ModelForm):
    class Meta:
        model = BuyerProfile
        fields = ('bio','location')

  

class ManagerForm(forms.ModelForm):
    class Meta:
        model = ManagerProfile
        fields = ('nursery_name',)