# Generated by Django 3.2 on 2022-08-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="ticket_title",
            field=models.CharField(
                blank=True, help_text="Ticket PyCon Africa", max_length=250, null=True
            ),
        ),
    ]
