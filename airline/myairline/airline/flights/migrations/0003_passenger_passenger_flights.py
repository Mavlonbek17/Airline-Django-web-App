# Generated by Django 4.0 on 2022-03-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_passenger'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='passenger_flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight'),
        ),
    ]
