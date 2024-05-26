from django import forms
from .models import Agent, Medicament, Achat

# class AgentForm(forms.ModelForm):
#     class Meta:
#         model = Agent
#         fields = ['nom', 'genre', 'phone', 'email']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class AgentForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = ['email', 'nom', 'genre', 'phone', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['nom'].required = True
        self.fields['genre'].required = True
        self.fields['phone'].required = True
        self.fields['password'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['agent', 'medicament', 'quantite']

# Medicament formModel
class MedicamentForm(forms.ModelForm):
    # nom = forms.CharField(label="Nom")
    # description = forms.CharField(label="Description", widget=forms.Textarea)
    # prix = forms.DecimalField(label="Prix")
    # stock = forms.IntegerField(label="Stock")
    date_exp = forms.DateField(label="Date d'expiration", widget=forms.DateInput(attrs={'type': 'date'}))
    # image = forms.ImageField(label="Image", widget=forms.ImageField)
    class Meta:
        model = Medicament
        fields = ['nom', 'description','image', 'prix', 'stock', 'date_exp']

# Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['u_name', 'profile_img']
        labels = {'u_name' : 'Username', 'profile_img': 'Picture'}