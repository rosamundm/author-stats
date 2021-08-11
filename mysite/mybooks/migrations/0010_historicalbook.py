# Generated by Django 3.0.7 on 2020-11-29 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mybooks", "0009_auto_20201122_1925"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalBook",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "date_added",
                    models.DateTimeField(default=django.utils.timezone.now, null=True),
                ),
                (
                    "last_updated",
                    models.DateTimeField(
                        blank=True, db_index=True, editable=False, null=True
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="A working title is great!", max_length=50, null=True
                    ),
                ),
                ("synopsis", models.TextField(help_text="What's it about?", null=True)),
                (
                    "wordcount",
                    models.IntegerField(
                        help_text="Your current word count",
                        null=True,
                        verbose_name="Word count",
                    ),
                ),
                (
                    "goalwordcount",
                    models.IntegerField(
                        help_text="What are you aiming for?",
                        null=True,
                        verbose_name="Goal word count",
                    ),
                ),
                (
                    "review",
                    models.TextField(help_text="Add any extra notes here", null=True),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical book",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
