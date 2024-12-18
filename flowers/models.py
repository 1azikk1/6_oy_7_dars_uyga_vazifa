from django.db import models


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
    photo = models.ImageField(upload_to='flowers/photos')
    is_available = models.BooleanField(default=True, verbose_name="Mavjud yoki Yoq", help_text="Galochka turgan holatda mavjud aks holda esa mavjud emas!")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Tur nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gul '
        verbose_name_plural = 'Gullar'
        ordering = ('created_at',)
