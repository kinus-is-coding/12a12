# Generated by Django 5.1.1 on 2024-09-08 14:44

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_remove_note_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="image_url",
            field=models.ImageField(
                blank=True, null=True, upload_to=base.models.upload_to
            ),
        ),
    ]
