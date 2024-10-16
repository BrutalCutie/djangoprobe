from django.db import models


class Product(models.Model):
    """
    Model Fields: name, descr, img, category, price, checkbox
    """
    name = models.CharField(max_length=30, verbose_name="Наименование")
    descr = models.TextField(verbose_name="Описание", blank=True)
    img = models.ImageField(verbose_name='Изображение', blank=True, upload_to='photos/')
    category = models.ForeignKey(to='Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 related_name='products')
    price = models.IntegerField(verbose_name='Цена')
    checkbox = models.BooleanField(verbose_name="Признак публикации", default=True)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время последнего изменения', auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Category(models.Model):
    """
    Model Fields: name, descr
    """

    name = models.CharField(max_length=100, verbose_name='Наименование')
    descr = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


