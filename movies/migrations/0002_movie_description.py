# Generated by Django 5.1.7 on 2025-03-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
