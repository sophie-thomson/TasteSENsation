# Generated by Django 4.2.16 on 2024-09-25 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('source_site', models.CharField(choices=[('Accessible Chef', 'Accessible Chef'), ('CookABILITY', 'CookABILITY')])),
                ('original_recipe', models.CharField()),
                ('baking', models.BooleanField(default=False)),
                ('mixing', models.BooleanField(default=False)),
                ('frying', models.BooleanField(default=False)),
                ('straining', models.BooleanField(default=False)),
                ('microwaving', models.BooleanField(default=False)),
                ('whisking', models.BooleanField(default=False)),
                ('chopping', models.BooleanField(default=False)),
                ('hob_use', models.BooleanField(default=False)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cooked_status', models.IntegerField(choices=[(0, 'Not Cooked'), (1, 'Cooked')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_selection', models.CharField(choices=[('Love this recipe!', 'Love this recipe!'), ('Delicious and easy to make.', 'Delicious and easy to make.'), ("OK, but probably won't make again.", "OK, but probably won't make again."), ('Too difficult for me, but might be OK for others', 'Too difficult for me, but might be OK for others')])),
                ('own_comment', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cookbook.recipe')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
