# Generated by Django 4.1.7 on 2023-03-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
