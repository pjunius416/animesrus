# Generated by Django 2.2 on 2021-11-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]