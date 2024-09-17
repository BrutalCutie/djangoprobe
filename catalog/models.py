from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    descr = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey(to='Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 related_name='products')

    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Время создания', default='now')
    updated_at = models.DateTimeField(verbose_name='Время последнего изменения')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        vebose_name = 'Продукт'
        vebose_name_plural = 'Продукты'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    descr = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        vebose_name = 'Категория'
        vebose_name_plural = 'Категории'
        ordering = ['name']


