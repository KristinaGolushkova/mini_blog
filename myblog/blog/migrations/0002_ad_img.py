# Generated by Django 4.1.5 on 2023-01-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Фото товара'),
            preserve_default=False,
        ),
    ]