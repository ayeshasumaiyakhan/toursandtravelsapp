# Generated by Django 2.2.5 on 2019-11-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0005_auto_20191118_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user_email',
            field=models.EmailField(max_length=30),
        ),
    ]