# Generated by Django 2.0.2 on 2018-07-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.CharField(choices=[('booked', 'Booked'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('canceled', 'Canceled'), ('timeout', 'Timeout'), ('completed', 'Completed')], default='Male', max_length=255),
        ),
    ]
