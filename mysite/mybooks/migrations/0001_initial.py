# Generated by Django 3.0.6 on 2020-06-21 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text='A working title is great!', max_length=50, null=True)),
                ('synopsis', models.TextField(help_text="What's it about?", null=True)),
                ('wordcount', models.IntegerField(help_text='Your word count when you added this title', null=True)),
                ('goalwordcount', models.IntegerField(null=True)),
                ('review', models.TextField(help_text='Any good so far?', null=True)),
            ],
        ),
    ]
