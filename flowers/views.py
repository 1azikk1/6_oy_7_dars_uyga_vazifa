from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Flowers, Species
from .forms import SpeciesForm, FlowerForm

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


def add_species(request):
    if request.method == 'POST':
        form = SpeciesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            species = Species.objects.create(**form.cleaned_data)
            print(species, "qo'shildi!")

    form = SpeciesForm()
    context = {
        'form': form,
        'title': "O'simlik turi qo'shish"
    }
    return render(request, 'add_species.html', context)


def add_flowers(request):
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flowers = Flowers.objects.create(**form.cleaned_data)
            print(flowers, "qo'shildi!")

    form = FlowerForm()
    context = {
        'form': form,
        'title': "Gul qo'shish"
    }
    return render(request, 'add_flowers.html', context)
