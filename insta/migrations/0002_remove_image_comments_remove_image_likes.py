# Generated by Django 4.0.3 on 2022-03-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
    ]
