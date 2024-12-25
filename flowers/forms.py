from django import forms
from .models import Species


class SpeciesForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tur nomini kiriting'
    }), label='Tur nomi')


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

