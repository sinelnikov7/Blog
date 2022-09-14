from django.db import models


class Genres(models.Model):

    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Название категории')
    info = models.TextField(verbose_name='Информация о категории')

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=100, unique=True,
                            verbose_name='Название города')
    info = models.TextField(verbose_name='Информация', unique=True)

    def __str__(self):
        return self.name


class Writer(models.Model):

    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    city = models.ForeignKey(City, related_name='writers',
                             verbose_name='Место рождения',
                             on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genres, related_name='authors')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
# Create your models here.
