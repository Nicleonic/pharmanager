from django.contrib import admin
# import the models
from .models import *

# Register your models here.
admin.site.register(Medicament)
admin.site.register(Agent)
admin.site.register(Achat)