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