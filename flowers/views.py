from django.shortcuts import render, get_object_or_404, redirect
from .models import Flowers, Species,Comment
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


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
        'title': f"{flower.name} haqida ma'lumotlar",
        'form': CommentForm(),
        'comments': Comment.objects.filter(flower_id=flower_id)
    }

    return render(request, 'detail.html', context)


def add_species(request):
    if request.method == 'POST':
        form = SpeciesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            species = form.create()
            messages.success(request, "Tur muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')
    else:
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
            flowers = form.create()
            messages.success(request, "Gul muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')
    else:
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
            flower = form.update(flower)
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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password_confirm == password:
                User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, "Muvaffaqiyatli tarzda saytimizga kirdingiz!")
                return redirect('login_view')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'title': "Sign Up Page"
    }
    return render(request, 'auth/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            messages.success(request, f"{username} Tabriklaymiz!!!Web sahifamizga kirdingiz!")
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': "Login Page"
    }
    return render(request, 'auth/login.html', context)


def logout_page(request):
    logout(request)
    messages.warning(request, "Web sahifamizdan chiqib ketdingiz!")
    return redirect('login_view')


def comment_save(request, flower_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(data=request.POST)
            if form.is_valid():
                flower = get_object_or_404(Flowers, pk=flower_id)
                Comment.objects.create(
                    text=form.cleaned_data.get('text'),
                    author=request.user,
                    flower=flower
                )
                messages.success(request, "Izoh qo'shildi!")

            return redirect('detail_flowers', flower_id=flower_id)

    messages.error(request, "Izoh qo'shish uchun avval saytga kiring!!!")
    return redirect('login_view')


def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_id)
        if request.user == comment.author or request.user.is_superuser:
            flower = comment.flower.pk
            comment.delete()
            messages.success(request, "Izoh o'chirildi!")
            return redirect('detail_flowers', flower_id=flower)

        messages.error(request, "Izohni o'chirsh uchun avval login qiling!")
        return redirect('login_view')


def comment_update(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_id)
        flower_id = comment.flower.id
        if request.user == comment.author or request.user.is_superuser:
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    form.update(comment)

                    messages.success(request, "Izoh muvaffaqiyatli o'zgartirildi.")
                    return redirect('detail_flowers', flower_id=flower_id)

            else:
                form = CommentForm(initial={'text': comment.text})

            context = {
                'flower': comment.flower,
                'form': form,
                'title': f"{comment.flower}: izohlar!",
            }

            return render(request, 'detail.html', context)

    else:
        messages.error(request, "Avval web sahifaga login qilishingiz kerak!")
        return redirect('login_view')
