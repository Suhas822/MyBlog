# Generated by Django 4.1.3 on 2024-01-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogmng', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
