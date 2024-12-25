from django.shortcuts import render, get_object_or_404, redirect
from .models import Flowers, Species
from .forms import SpeciesForm, FlowerForm
from django.contrib import messages


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
            messages.success(request, "Tur muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')

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
            messages.success(request, "Gul muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')

    form = FlowerForm()
    context = {
        'form': form,
        'title': "Gul qo'shish"
    }
    return render(request, 'add_flowers.html', context)


def update_flower(request, flower_id):
    flower = Flowers.objects.get(pk=flower_id)
    if request.method == 'POST':
        form = FlowerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            flower.name = form.cleaned_data.get('name')
            flower.about = form.cleaned_data.get('about')
            flower.photo = form.cleaned_data.get('photo') if form.cleaned_data.get('photo') else flower.photo
            flower.is_available = form.cleaned_data.get('is_available')
            flower.species = form.cleaned_data.get('species')
            flower.save()
            messages.success(request, "Gul haqida ma'lumotlar muvaffaqiyatli tarzda yangilandi!")
            return redirect('detail_flowers', flower_id=flower.pk)

    form = FlowerForm(initial={
        'name': flower.name,
        'about': flower.about,
        'photo': flower.photo,
        'is_available': flower.is_available,
        'species': flower.species,
    })
    context = {
        'form': form,
        'photo': flower.photo,
        'title': f"{flower.name}: ma'lumotlarni yangilash!"
    }
    return render(request, 'add_flowers.html', context)


def delete_flower(request, flower_id):
    flower = Flowers.objects.get(pk=flower_id)
    if request.method == 'POST':
        flower.delete()
        messages.success(request, "Gul muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'flower': flower,
        'title': f"{flower.name}: Gulni o'chirish!"
    }
    messages.warning(request, "Ushbu gul ni o'chirib tashlamoqchimisiz!")
    return render(request, 'confirm_delete.html', context)
