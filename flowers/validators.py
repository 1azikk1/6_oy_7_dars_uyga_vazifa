from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.hashers import check_password


# username validator
def username_validator(value):
    if ' ' in value:
        raise ValidationError("Foydalanuchi nomi bo'sh joylarsiz yozilishi kerak!")


def user_availability_check(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError("Ushbu foydalanuvchi nomi bilan ro'yhatdan o'tilgan!")


def email_validator(value: str):
    if value.endswith('gmail.com'):
        raise ValidationError("Noto'g'ri shakldagi email kiritldi!")
    elif "@" not in value:
        raise ValidationError("Emailda @ belgisi bo'lishi shart!")


# password length
def password_length(value):
    if len(value) < 8:
        raise ValidationError("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")


# login form
def user_availability(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError("Bunday foydalanuvchi mavjud emas!")


def password_validator(username, password):
    user = User.objects.get(username=username)
    if not check_password(password, user.password):
        raise ValidationError("Kiritilgan parol noto‘g‘ri!")


def comment_length(value):
    if len(value) > 1000:
        raise ValidationError("Kiritilgan izoh uzunligi belgilangan izohdan oshib ketdi!")


# flower name validator
def flower_validator(value):
    if Flowers.objects.filter(name=value).exists():
        raise ValidationError("Bunday gul mavjud!")


# species name validator
def species_validator(value):
    if Species.objects.filter(name=value).exists():
        raise ValidationError("Bunday gul turi mavjud!")
