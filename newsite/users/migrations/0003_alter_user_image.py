# Generated by Django 3.2.4 on 2021-06-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210610_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='placeholder.jpg', upload_to='profile_pics'),
        ),
    ]
