# Generated by Django 4.2.7 on 2023-12-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
