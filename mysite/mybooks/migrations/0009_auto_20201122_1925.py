# Generated by Django 3.0.7 on 2020-11-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mybooks", "0008_auto_20200629_0715"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, db_index=True, null=True),
        ),
    ]