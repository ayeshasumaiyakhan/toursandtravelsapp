# Generated by Django 2.2.5 on 2019-11-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thankyou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry', models.CharField(max_length=100)),
                ('satisfied', models.CharField(help_text='If your satisfied enter Y, if not enter N ', max_length=1)),
            ],
        ),
    ]
