# Generated by Django 5.1.3 on 2024-11-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0004_alter_category_slug_alter_tag_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="content_words_count",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
