# Generated by Django 4.0 on 2022-03-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
