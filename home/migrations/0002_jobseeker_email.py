# Generated by Django 5.0 on 2023-12-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobseeker",
            name="email",
            field=models.EmailField(
                default="jobseeker@gmail.com", max_length=254, unique=True
            ),
        ),
    ]
