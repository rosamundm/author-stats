# Generated by Django 3.0.6 on 2020-06-25 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0003_auto_20200625_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]