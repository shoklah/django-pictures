# Generated by Django 3.0.3 on 2020-02-24 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20200224_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='album',
        ),
    ]
