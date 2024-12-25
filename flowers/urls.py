from django.urls import path
from .views import home, flowers_by_species, detail_flowers, add_species, add_flowers, update_flower, delete_flower

urlpatterns = [
    path('', home, name='home'),
    path('species/<int:species_id>/', flowers_by_species, name='flowers_by_species'),
    path('flower/<int:flower_id>/', detail_flowers, name='detail_flowers'),
    path('flower/<int:flower_id>/update/', update_flower, name='update_flower'),
    path('flower/<int:flower_id>/delete/', delete_flower, name='delete_flower'),
    path('species/add/', add_species, name='add_species'),
    path('flowers/add/', add_flowers, name='add_flowers'),
]
