# Generated by Django 2.0.2 on 2018-07-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20180726_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='overview',
            field=models.TextField(blank=True),
        ),
    ]
