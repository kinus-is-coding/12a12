# Generated by Django 5.1.1 on 2024-09-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_note_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="img/", verbose_name="Image"
            ),
        ),
    ]
