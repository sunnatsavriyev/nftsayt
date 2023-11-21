from dataclasses import field
from .models import *
from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    UserName = forms.CharField(
        label='User Name',
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs = {'placeholder':'User Name'}),
    )
    password = forms.CharField(
        label='password',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'password','type':'password'})
    )

    
class AddNFTform(forms.ModelForm):
    class Meta:
        model = AddNftModel
        fields = '__all__'
        exclude = ['user']


class EditImgForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['image']
