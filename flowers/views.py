from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Flowers, Species


def home(request):
    flowers = Flowers.objects.all()
    context = {
        'flowers': flowers,
        'title': "Barcha gullar"
    }
    return render(request, 'index.html', context)


def flowers_by_species(request, species_id):
    flowers = Flowers.objects.filter(species_id=species_id)
    species = Species.objects.get(pk=species_id)
    context = {
        'flowers': flowers,
        'title': f'{species.name}: Barcha gullar'
    }
    return render(request, 'index.html', context)


def detail_flowers(request, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id)
    flower.views += 1
    flower.save()
    context = {
        'flower': flower,
        'title': f"{flower.name} haqida ma'lumotlar"
    }
    return render(request, 'detail.html', context)

