# Generated by Django 3.0.6 on 2020-07-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200630_2010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterRecipient',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
