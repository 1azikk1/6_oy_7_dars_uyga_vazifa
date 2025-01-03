from django.urls import path
from .views import (home, flowers_by_species, detail_flowers, add_species, add_flowers, update_flower,
                    delete_flower, register, login_view, logout_page, comment_save, delete_comment, comment_update)

urlpatterns = [
    path('', home, name='home'),
    path('species/<int:species_id>/', flowers_by_species, name='flowers_by_species'),
    path('flower/<int:flower_id>/', detail_flowers, name='detail_flowers'),
    path('flower/<int:flower_id>/update/', update_flower, name='update_flower'),
    path('flower/<int:flower_id>/delete/', delete_flower, name='delete_flower'),
    path('species/add/', add_species, name='add_species'),
    path('flowers/add/', add_flowers, name='add_flowers'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_page, name='logout_page'),
    path('flower/<int:flower_id>/comment/update/', comment_save, name='comment_save'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/update/', comment_update, name='comment_update'),
]
