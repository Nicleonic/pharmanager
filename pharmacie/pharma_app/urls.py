from django.contrib import admin
from django.urls import path
import pharma_app.views as ph_views


app_name = 'pharma_app'
urlpatterns = [
    path('', ph_views.index, name='index'),
    path('about', ph_views.about, name='about'),
    path('item/<int:item_id>/', ph_views.item, name='item_view')

]
