# Generated by Django 5.1.4 on 2024-12-30 13:23

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(blank=True, default=blog.models.get_default_blog_image, null=True, upload_to=blog.models.get_blog_image_filepath, verbose_name='تصویر'),
        ),
    ]