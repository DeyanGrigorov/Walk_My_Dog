# Generated by Django 3.2.5 on 2021-08-04 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('walkmydog_auth', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='walkmydog_auth.walkmydoguser')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=12)),
                ('last_name', models.CharField(blank=True, max_length=13)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
