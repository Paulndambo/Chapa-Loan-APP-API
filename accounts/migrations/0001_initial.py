# Generated by Django 4.0.5 on 2022-06-23 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('femail', 'Female')], max_length=200)),
                ('date_of_birth', models.DateField()),
                ('postal_code', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
