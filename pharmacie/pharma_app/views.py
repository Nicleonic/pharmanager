from django.shortcuts import render
from .models import Medicament

# Create your views here.
def index(request):
    title = "Home"
    medocs = Medicament.objects.all()
    return render(request, "pharma_app/index.html", {"title" : title, "medicaments" : medocs })

def item(request, item_id):
    medoc = Medicament.objects.get(id=item_id)
    
    return render(request, "pharma_app/item.html", {'title': medoc.nom, 'medoc': medoc})