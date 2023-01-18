# Generated by Django 4.1.5 on 2023-01-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schema_name', models.CharField(max_length=100)),
                ('subdomain', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]