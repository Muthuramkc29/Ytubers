# Generated by Django 3.2.8 on 2021-10-27 11:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtuber',
            name='role',
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('Canon', 'Canon'), ('Nikon', 'Nikon'), ('Fujji', 'Fujji'), ('Others', 'Others')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('Code', 'Code'), ('Mobile_review', 'Mobile_review'), ('Gaming', 'Gaming'), ('Vlogs', 'Vlogs'), ('Cooking', 'Cooking'), ('Comedy', 'Comedy')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('Solo', 'Solo'), ('Small', 'Small'), ('Large', 'Large')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]