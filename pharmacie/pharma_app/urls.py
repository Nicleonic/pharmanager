from django.contrib import admin
from django.urls import path
import pharma_app.views as ph_views


app_name = 'pharma_app'
urlpatterns = [
    path('', ph_views.index, name='index'),
    path('about', ph_views.about, name='about'),
    path('item/<int:item_id>/', ph_views.item, name='item_view'),
    # add item
    path('item/add/', ph_views.send_medicament, name='post_item'),
    # edit item
    path('item/edit/<int:medicament_id>/', ph_views.edit_medicament, name='edit_item'),
    # delet item
    path('item/delete/<int:medicament_id>/', ph_views.delete_medicament, name='delete_item'),
    path('profile_edit/', ph_views.profile, name='profile_edit'),
    path('profile_crea/', ph_views.profile_crea, name='profile_crea'),


    
    path('search-medicament/', ph_views.search_medicament, name='finder'),


]
