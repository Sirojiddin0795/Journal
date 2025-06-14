# Generated by Django 5.2.2 on 2025-06-11 12:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('question_uz', models.CharField(max_length=300, null=True)),
                ('question_en', models.CharField(max_length=300, null=True)),
                ('answer', ckeditor.fields.RichTextField()),
                ('answer_uz', ckeditor.fields.RichTextField(null=True)),
                ('answer_en', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
