from django.db import models
from django.contrib.auth.models import User


class Species(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Tur nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tur '
        verbose_name_plural = 'Turlar'


class Flowers(models.Model):
    name = models.CharField(max_length=50, verbose_name='Gul nomi')
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    photo = models.ImageField(upload_to='flowers/photos', blank=True, null=True)
    is_available = models.BooleanField(default=True, verbose_name="Mavjud yoki Yoq", help_text="Galochka turgan holatda mavjud aks holda esa mavjud emas!")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Tur nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gul '
        verbose_name_plural = 'Gullar'
        ordering = ('created_at',)


class Comment(models.Model):
    text = models.CharField(max_length=1000, verbose_name='Izoh Matni')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}|{self.text[:20]}|{self.flower.name}"

    class Meta:
        verbose_name = 'izoh '
        verbose_name_plural = 'izohlar'
        ordering = ['-created']
