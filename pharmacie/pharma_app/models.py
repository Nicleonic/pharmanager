from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



class Medicament(models.Model):
    class Meta:
        permissions = [
            ("publish_medicament", "Can publish a Medecine"),
            ("sell_medicament", "Can sell a Medecine")
        ]
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_exp = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Agent(models.Model):
    nom = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Achat(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Achat {self.id} - {self.medicament.nom} par {self.agent.nom} quantité {self.quantite}"



# ==================================== Permissions

# Créer le groupe "SuperAgents"
# SuperAgents, created = Group.objects.get_or_create(name='SuperAgents')
# Créer le groupe "Seller"
# Seller, created = Group.objects.get_or_create(name="Seller")
# Seller.save()


# Ajouter un utilisateur existant au groupe "Agents"
# johnson = User.objects.get(username='johnson')
# SuperAgents.user_set.add(johnson)

# publish_permission = Permission.objects.get(codename='publish_medicament')
# sell_permission = Permission.objects.get(codename="sell_medicament")

# Ajoutez la permission au groupe "SuperAgents"
# SuperAgents.permissions.add(publish_permission)

# Ajoutez la permission au groupe "Seller"
# Seller.permissions.add(sell_permission)