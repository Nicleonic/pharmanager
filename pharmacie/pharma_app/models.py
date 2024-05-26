from typing import Iterable
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from pharmacie import settings

from django.utils.translation import gettext_lazy as _

User = get_user_model()
# User = settings.AUTH_USER_MODEL;

class Medicament(models.Model):
    class Meta:
        permissions = [
            ("publish_medicament", "Can publish a Medecine"),
            ("sell_medicament", "Can sell a Medecine")
        ]
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="medicament_images", null=True, blank=True) # Champ d'image ajouté
    # image = models.ImageField(upload_to='medicament_images/')  # Champ d'image ajouté
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    date_exp = models.DateField(blank=True, null=True)
    #creator = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.get(username='Johnson').id) #NEW
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
# Select Fiels ============================================
class AgentGender(models.TextChoices):
    Masculin = "Masculin"
    Feminin = "Feminin"
    # =====================================================




class Agent(models.Model):
    nom = models.CharField(max_length=100)
    password = models.CharField(_('password'), max_length=128)
    image = models.ImageField(upload_to="agent_images", null=True, blank=True) # Champ d'image ajouté
    genre = models.CharField(max_length=10, choices=AgentGender.choices)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return self.nom

class Achat(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Achat {self.id} - {self.medicament.nom} par {self.agent.nom} quantité {self.quantite}"


# CUSTOM User Profile

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_images", null=True, blank=True)
    u_name = models.CharField(max_length=100,null=False, blank=False)
    date_crea = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - Profile'
    
    def profile_crea(user):
        return user       

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 300 , 300

        if self.profile_img:
            image = Image.open(self.profile_img.path)
            if image.width > 300 or image.height > 300:
                out_size = (300, 300)
                image.thumbnail(out_size)
                image.save(self.profile_img.path)

'''    def save(self, **kwargs):
        do_something()
        super().save(**kwargs) # Call the "real" save() method.
        do_something_else()'''

# CUSTOM USER MODEL
'''from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )'''
# ==================================== Permissions

# Créer le groupe "SuperAgents"
# SuperAgents, created = Group.objects.get_or_create(name='SuperAgents')
# SuperAgents.save()
# Créer le groupe "Seller"
# Seller, created = Group.objects.get_or_create(name="Seller")
# Seller.save()


# Ajouter un utilisateur existant au groupe "Agents"
# johnson = User.objects.get(username='Johnson')
# SuperAgents.user_set.add(johnson)

# publish_permission = Permission.objects.get(codename='publish_medicament')
# sell_permission = Permission.objects.get(codename="sell_medicament")

# Ajoutez la permission au groupe "SuperAgents"
# SuperAgents.permissions.add(publish_permission)

# Ajoutez la permission au groupe "Seller"
# Seller.permissions.add(sell_permission)



# AUTHENTIFICATION
'''
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class AgentUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), max_length=128)
    nom = models.CharField(_('nom'), max_length=100)
    genre = models.CharField(_('genre'), max_length=10, choices=AgentGender.choices)
    phone = models.CharField(_('phone'), max_length=20)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'genre', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.emai'''