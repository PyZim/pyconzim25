# Generated by Django 5.0.2 on 2024-05-07 13:33

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0008_iocmember_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="about",
            name="section_four",
            field=markdownx.models.MarkdownxField(
                blank=True,
                default="",
                help_text="[Supports Markdown] - More about PyCon Africa.",
            ),
        ),
    ]
