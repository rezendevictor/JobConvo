from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .models import User,Profile

from vagas.enums import FaixaSalarial,EscolaridadeMin

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    CHOICES=[(0,'Empresa'),
         (1,'Candidato')]

    tipo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    escolaridade_min = models.CharField(
     max_length= 50,
      choices= EscolaridadeMin.choices)

    faixa_salarial = models.CharField(
      max_length=100, 
      choices = FaixaSalarial.choices)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tipo','faixa_salarial','escolaridade_min']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','faixa_salarial','escolaridade_min']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']