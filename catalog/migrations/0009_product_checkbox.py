# Generated by Django 5.1.1 on 2024-10-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='checkbox',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
    ]