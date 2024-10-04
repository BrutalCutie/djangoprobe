from django.db import models


class BlogModel(models.Model):
    BOOLEAN_CHOICES = [
        (True, 'Да'),
        (False, 'Нет'),
    ]

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    inner = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(verbose_name="Превью", upload_to='preview/', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(verbose_name="Признак публикации", choices=BOOLEAN_CHOICES)
    views = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0, auto_created=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
