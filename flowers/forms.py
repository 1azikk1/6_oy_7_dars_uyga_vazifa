from django import forms
from .models import Species, Flowers


class SpeciesForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tur nomini kiriting'
    }), label='Tur nomi')

    def create(self):
        species = Species.objects.create(**self.cleaned_data)
        return species


class FlowerForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'gul nomini kiriting',
        'class': 'form-control'
    }), label='Gul nomi')
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
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'form3Example3cg',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cg',
        'class': 'form-control form-control-lg'
    }))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cdg',
        'class': 'form-control form-control-lg'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'typeEmailX-2',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'typePasswordX-2',
        'class': 'form-control form-control-lg'
    }))

