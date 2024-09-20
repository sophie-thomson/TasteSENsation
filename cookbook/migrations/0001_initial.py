# Generated by Django 4.2.16 on 2024-09-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('source_site', models.CharField(max_length=200)),
                ('baking', models.BooleanField(default=False)),
                ('mixing', models.BooleanField(default=False)),
                ('frying', models.BooleanField(default=False)),
                ('straining', models.BooleanField(default=False)),
                ('mashing', models.BooleanField(default=False)),
                ('whisking', models.BooleanField(default=False)),
                ('chopping', models.BooleanField(default=False)),
                ('hob_use', models.BooleanField(default=False)),
                ('average_rating', models.IntegerField(default=0)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cooked_status', models.IntegerField(choices=[(0, 'Not Cooked'), (1, 'Cooked')], default=0)),
                ('want_to_try_tag', models.BooleanField(default=False)),
                ('dislike_tag', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
