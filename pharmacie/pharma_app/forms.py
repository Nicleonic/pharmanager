from django import forms
from .models import Agent, Medicament, Achat

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['nom', 'genre', 'phone', 'email']

class AchatForm(forms.ModelForm):
    class Meta:
        model = Achat
        fields = ['agent', 'medicament', 'quantite']

# Medicament formModel
class MedicamentForm(forms.ModelForm):
    nom = forms.CharField(label="Nom")
    description = forms.CharField(label="Description", widget=forms.Textarea)
    prix = forms.DecimalField(label="Prix")
    stock = forms.IntegerField(label="Stock")
    date_exp = forms.DateField(label="Date d'expiration", widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Medicament
        fields = ['nom', 'description', 'prix', 'stock', 'date_exp']