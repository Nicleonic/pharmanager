from django.db import models

from django.contrib.auth.models import Group

# Create your models here.
# To create a group

# sel = Group(name="Seller")
# sel.save()

# To get a group
# seller = Group.objects.get(name="Seller")


# To get all users in a group : ( as a QuerySet)
# sellers = seller.user_set.all()



# custom usermodel

# class CustomUser(AbstractUser):
#     is_voter = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_candidate = models.BooleanField(default=False)
#     profile_picture = models.ImageField(upload_to='prfile_pictures', blank=True,null=True)
#     date_of_birth = models.DateField(blank=True, null=True)