# Generated by Django 2.2.5 on 2019-11-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_auto_20191118_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='address',
            field=models.TextField(max_length=100),
        ),
    ]
