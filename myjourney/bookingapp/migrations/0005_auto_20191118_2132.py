# Generated by Django 2.2.5 on 2019-11-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0004_thankyou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thankyou',
            name='enquiry',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='thankyou',
            name='satisfied',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], help_text='If your satisfied with our service select yes', max_length=1),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]