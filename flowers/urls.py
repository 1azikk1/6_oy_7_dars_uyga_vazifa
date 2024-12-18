from django.urls import path
from .views import home, flowers_by_species, detail_flowers

urlpatterns = [
    path('', home, name='home'),
    path('species/<int:species_id>/', flowers_by_species, name='flowers_by_species'),
    path('flower/<int:flower_id>/', detail_flowers, name='detail_flowers'),
]
