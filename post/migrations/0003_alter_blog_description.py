# Generated by Django 4.1.6 on 2023-04-07 03:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_blog_slug_alter_category_slug_alter_tag_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]