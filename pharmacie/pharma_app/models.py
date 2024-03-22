from django.db import models

# Create your models here.
# Create your models here.

class Medicament(models.Model):
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
