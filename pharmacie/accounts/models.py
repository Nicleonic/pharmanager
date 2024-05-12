from django.db import models

from django.contrib.auth.models import Group

# Create your models here.
# To create a group

# sel = Group(name="seller")
# sel.save()

# To get a group
# seller = Group.objects.get(name="seller")


# To get all users in a group : ( as a QuerySet)
# sellers = seller.user_set.all()