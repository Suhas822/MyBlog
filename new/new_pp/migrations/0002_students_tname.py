# Generated by Django 4.1.3 on 2024-01-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_pp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='tname',
            field=models.CharField(default=3, max_length=20),
            preserve_default=False,
        ),
    ]
