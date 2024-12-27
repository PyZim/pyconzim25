# Generated by Django 3.2 on 2022-08-17 12:05

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Venue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="Venue of PyCon Africa", max_length=250),
                ),
                (
                    "content",
                    markdownx.models.MarkdownxField(
                        default="", help_text="[Supports Markdown] - Content."
                    ),
                ),
                (
                    "content_two",
                    markdownx.models.MarkdownxField(
                        default="", help_text="[Supports Markdown] - Content side two."
                    ),
                ),
                (
                    "link_to_preview_video_url",
                    embed_video.fields.EmbedVideoField(
                        blank=True,
                        default="",
                        help_text="Link to Preview video on your Youtube or Google drive",
                    ),
                ),
                (
                    "google_map",
                    models.CharField(
                        default="", help_text="Venue Google map ID", max_length=500
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        default="", help_text="Location of Venue", max_length=250
                    ),
                ),
                (
                    "location_address",
                    models.CharField(
                        default="", help_text="Location of Venue", max_length=250
                    ),
                ),
                (
                    "location_website",
                    models.URLField(
                        blank=True, default="", help_text="Venue's website if any"
                    ),
                ),
                ("image_one", models.URLField(default="", help_text="Link to image")),
                ("image_two", models.URLField(default="", help_text="Link to image")),
                ("first_day_of_event", models.DateTimeField(blank=True, null=True)),
                ("last_day_of_event", models.DateTimeField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "venue",
                "verbose_name_plural": "venues",
                "unique_together": {("name",)},
            },
        ),
        migrations.CreateModel(
            name="Travel_Advice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Travel Advice PyCon Africa", max_length=250
                    ),
                ),
                (
                    "advice",
                    markdownx.models.MarkdownxField(
                        default="",
                        help_text="[Supports Markdown] - Travel Advice PyCon Africa.",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=django.contrib.auth.models.User,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="travel_advice",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "about_title",
                    models.CharField(help_text="About PyCon Africa", max_length=250),
                ),
                (
                    "about_image_one",
                    models.ImageField(
                        help_text="Upload your cover image or leave blank to use our default image",
                        upload_to="about_page",
                    ),
                ),
                (
                    "about_image_two",
                    models.URLField(default="", help_text="Link to image"),
                ),
                (
                    "section_one",
                    markdownx.models.MarkdownxField(
                        default="",
                        help_text="[Supports Markdown] - About PyCon Africa.",
                    ),
                ),
                (
                    "section_two",
                    markdownx.models.MarkdownxField(
                        default="",
                        help_text="[Supports Markdown] - About PyCon Africa.",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="about_us",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
