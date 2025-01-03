from django import forms
from .models import Species, Flowers, Comment
from .validators import *
from django.core.validators import *


class SpeciesForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tur nomini kiriting'
    }), label='Tur nomi', validators=[species_validator])

    def create(self):
        species = Species.objects.create(**self.cleaned_data)
        return species


class FlowerForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'gul nomini kiriting',
        'class': 'form-control'
    }), label='Gul nomi', validators=[flower_validator])
    about = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "gul haqida ma'lumot kiriting",
        'class': 'form-control'
    }), label='Gul haqida')
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), label='Gul rasmi', required=False)
    is_available = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
        'checked': 'checked'
    }), label="Mavjud yoki yo'q")
    species = forms.ModelChoiceField(queryset=Species.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select'
    }), label="Bog'langan gul turi")

    def create(self):
        flowers = Flowers.objects.create(**self.cleaned_data)
        return flowers

    def update(self, flower):
        flower.name = self.cleaned_data.get('name')
        flower.about = self.cleaned_data.get('about')
        flower.photo = self.cleaned_data.get('photo') if self.cleaned_data.get('photo') else flower.photo
        flower.is_available = self.cleaned_data.get('is_available')
        flower.species = self.cleaned_data.get('species')
        flower.save()
        return flower


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'form3Example1cg',
        'class': 'form-control form-control-lg'
    }), validators=[username_validator, user_availability_check])
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'form3Example3cg',
        'class': 'form-control form-control-lg'
    }), validators=[EmailValidator])
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cg',
        'class': 'form-control form-control-lg'
    }))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cdg',
        'class': 'form-control form-control-lg'
    }))

    # password similarity check
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password_confirm != password:
            raise ValidationError("Parollar bir xil bo'lishi kerak!")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'typeEmailX-2',
        'class': 'form-control form-control-lg'
    }), validators=[username_validator, user_availability])
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'typePasswordX-2',
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                password_validator(username, password)
            except ValidationError as e:
                self.add_error('password', e.message)


class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Izoh kiriting...",
        'rows': 2
    }), label='Izoh', validators=[comment_length])

    def update(self, comment):
        comment.text = self.cleaned_data.get('text')
        comment.save()
        return comment
