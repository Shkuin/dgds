# Generated by Django 3.0.7 on 2023-06-04 17:03

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('platform', models.CharField(max_length=100)),
                ('poster', models.CharField(max_length=1000)),
                ('images', jsonfield.fields.JSONField()),
                ('price', models.FloatField()),
                ('token_id', models.CharField(max_length=100)),
                ('private_key', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
