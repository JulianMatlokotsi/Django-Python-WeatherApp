# Generated by Django 5.1.1 on 2024-10-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('condition', models.CharField(max_length=100)),
                ('recorded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]