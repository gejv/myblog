# Generated by Django 4.1.5 on 2023-01-17 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_works"),
    ]

    operations = [
        migrations.DeleteModel(name="Works",),
    ]