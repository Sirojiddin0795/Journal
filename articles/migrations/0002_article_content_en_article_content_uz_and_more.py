# Generated by Django 5.2.2 on 2025-06-09 20:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
