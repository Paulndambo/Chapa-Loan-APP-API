# Generated by Django 4.0.5 on 2022-06-23 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpesa_statement', models.FileField(blank=True, null=True, upload_to='mpesa_statements')),
                ('bank_statement', models.FileField(blank=True, null=True, upload_to='bank_statements')),
                ('proof_of_income', models.FileField(blank=True, null=True, upload_to='income_documents')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=200)),
                ('institution', models.CharField(blank=True, max_length=500, null=True)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField(null=True)),
                ('is_current', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]