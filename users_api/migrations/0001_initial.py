# Generated by Django 4.0.6 on 2022-07-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('number', models.CharField(max_length=13, unique=True)),
                ('role', models.CharField(choices=[('REGULAR', 'Regular'), ('ADMIN', 'Admin')], default='REGULAR', max_length=8)),
            ],
        ),
    ]
