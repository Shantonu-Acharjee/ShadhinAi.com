# Generated by Django 4.1.7 on 2023-03-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("post_thumbnail", models.ImageField(upload_to="posts/")),
                ("post_title", models.CharField(max_length=200)),
                ("post_url", models.CharField(max_length=200, unique=True)),
                ("post_short_description", models.CharField(max_length=200)),
                ("post_description", models.TextField()),
                ("post_date", models.DateTimeField(auto_now_add=True)),
                ("post_keyword", models.TextField()),
                ("post_Schema", models.TextField()),
            ],
        ),
    ]
