import django
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    # path('login/', django.auth.views.login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('create/', views.create_account, name='create'),
    path('profile/change/', views.change_profile, name='change-profile'),
    # path('logout/', views.logout_view, name='logout_'),
    # path('profile/logout/',views.logout_view, name='logout'),


    
]
