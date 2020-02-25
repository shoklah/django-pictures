# Generated by Django 3.0.3 on 2020-02-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('description', models.TextField(blank=True)),
                ('cover', models.ImageField(upload_to='images/')),
                ('public', models.BooleanField(default=False)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130)),
                ('image', models.ImageField(upload_to='images/')),
                ('album_id', models.BigIntegerField()),
                ('public', models.BooleanField(default=False)),
                ('user_id', models.CharField(max_length=255)),
            ],
        ),
    ]
