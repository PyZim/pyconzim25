# Generated by Django 3.2 on 2022-03-30 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("privacypolicy", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="privacy",
            options={"verbose_name": "privacy", "verbose_name_plural": "privacies"},
        ),
        migrations.AlterUniqueTogether(
            name="privacy",
            unique_together={("title",)},
        ),
    ]
