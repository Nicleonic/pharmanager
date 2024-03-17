from django.shortcuts import render,get_object_or_404
from .models import Medicament
from django.http import Http404

# Create your views here.
def index(request):
    title = "Home"
    medocs = Medicament.objects.all()
    return render(request, "pharma_app/index.html", {"title" : title, "medicaments" : medocs })

def item(request, item_id):
    # try:
    #     medoc = Medicament.objects.get(id=item_id)
    # except:
    #     raise Http404("Error 404")
    # medoc = Medicament.objects.get_or_404(id=item_id)
    medoc = get_object_or_404(Medicament, id=item_id)
    
    return render(request, "pharma_app/item.html", {"title": medoc.nom, 'medoc': medoc})


def about(request):
    title = "About P<Manager>"
    return render(request, "pharma_app/about.html",  {"title": title})