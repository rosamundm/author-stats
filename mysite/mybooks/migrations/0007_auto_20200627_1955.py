# Generated by Django 3.0.6 on 2020-06-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mybooks", "0006_auto_20200627_1917"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="last_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
