# Generated by Django 4.1.5 on 2023-01-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_story_date_now_story_date_time_now"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story", name="date_now", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="story", name="date_time_now", field=models.DateTimeField(),
        ),
    ]
