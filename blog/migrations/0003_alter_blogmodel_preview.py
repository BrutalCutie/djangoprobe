# Generated by Django 5.1.1 on 2024-10-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='preview',
            field=models.ImageField(blank=True, upload_to='preview/', verbose_name='Превью'),
        ),
    ]
