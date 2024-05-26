from django.shortcuts import redirect, render,get_object_or_404
from .models import Medicament, Profile
from django.http import JsonResponse
from .forms import *
from accounts.urls import *
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.views.generic import ListView


# Create your views here.
def error404_view(request, exception):
    title = 'error 404'
    return render(request, "base/404.html", {'title': title })

def search_medicament(request):
    search_term = request.GET.get('q')
    medicaments = Medicament.objects.filter(nom__icontains=search_term)
    results = [{'id': m.id,'nom': m.nom, 'quantite': m.stock} for m in medicaments]
    print("--------------------------------------------------------------")
    print(results)
    return JsonResponse(results, safe=False)

# ===========================================
def not_authenticated(user):
    return  user.is_authenticated

@user_passes_test(not_authenticated)
def index(request):
    title = "Home"
    medocs = Medicament.objects.all()
    profile = get_object_or_404(Profile, user=request.user.id)
    # paginator
    p = Paginator(medocs,12)
    page_number = request.GET.get("page")
    page_obj = p.get_page(page_number)

    
    
    return render(request, "pharma_app/index.html", {"title" : title, "medicaments" : page_obj,'profile' : profile, 'page_obj': page_obj })
# paginator
class medListView(ListView):
    paginate_by = 12
    model = Medicament




# end paginator



@login_required
@permission_required('pharma_app.view_medicament', raise_exception=True)
def item(request, item_id):
    # try:
    #     medoc = Medicament.objects.get(id=item_id)
    # except:
    #     raise Http404("Error 404")
    # medoc = Medicament.objects.get_or_404(id=item_id)
    medoc = get_object_or_404(Medicament, id=item_id)
    profile = get_object_or_404(Profile, user=request.user.id)
    print("Image de l'image ", medoc ,"  est ", medoc.nom ," : --> ", medoc.image )
    return render(request, "pharma_app/item.html", {"title": medoc.nom, 'medoc': medoc, 'profile': profile})


# post_item views (function) =============================================================================================

def log_medicament(medicament):
    with open('medicaments.log', 'a+') as f:
        f.write(f"Nom: {medicament.nom}\n")
        f.write(f"Description: {medicament.description}\n")
        f.write(f"Prix: {medicament.prix}\n")
        f.write(f"Stock: {medicament.stock}\n")
        f.write(f"Date d'expiration: {medicament.date_exp}\n")
        f.write("\n")

        
@permission_required('pharma_app.add_medicament', raise_exception=True)
def send_medicament(request):
    title = "Add Medecine"
    if request.method == "POST":
        form = MedicamentForm(request.POST, request.FILES)
        if form.is_valid():
            medecine_form = form.save(commit=False)
            medecine_form.creator = request.user
            medecine_form.save()
            log_medicament(form.instance)
            return redirect('/')
    else:
        form = MedicamentForm(request.GET)
    return render(request, 'pharma_app/add_item.html', { "form": form , "title": title })

# edit_item ======================================================================
@permission_required('pharma_app.change_medicament', raise_exception=True)
def edit_medicament(request, medicament_id):
    medicament = get_object_or_404(Medicament, pk=medicament_id)
    title = "Edit " + medicament.nom
    
    if request.method == "POST":
        form = MedicamentForm(request.POST,request.FILES, instance=medicament)
        if form.is_valid():
            form.save()
            # Gestion de la redirection après la modification réussie
            return redirect('/item/%s' % medicament_id)
    else:
        form = MedicamentForm(instance=medicament)

    return render(request, 'pharma_app/edit_item.html', {'form': form, "title": title})

# delete_item ======================================================================
@permission_required('pharma_app.delete_medicament', raise_exception=True)
def delete_medicament(request, medicament_id):
    # Récupérer l'objet Medicament à supprimer
    medicament = get_object_or_404(Medicament, pk=medicament_id)
    
    if request.method == "POST":
        # Supprimer l'objet Medicament de la base de données
        medicament.delete()
        # Gestion de la redirection après la suppression réussie
        return redirect('/')
    
    # Afficher la page de confirmation de suppression
    return render(request, 'pharma_app/delete_item.html', {'medicament': medicament , 'title': "delete "+medicament.nom})

def about(request):
    title = "About P<Manager>"
    print("UserAccount : ", request.user)
    return render(request, "pharma_app/about.html",  {"title": title, 'user': request.user})

# Profile Config
@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    
    user = request.user.id;
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Gestion de la redirection après la modification réussie
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'pharma_app/profile_edit.html', {'profile' : profile, 'form': form})

@login_required
def profile_crea(request):
    title = "Profile crea"
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            valid_form = form.save(commit=False)
            valid_form.user = request.user
            valid_form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(request.GET)
    return render(request, 'pharma_app/profile_crea.html', { "form": form , "title": title })