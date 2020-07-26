# Generated by Django 3.0.7 on 2020-07-26 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_auto_20200725_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenantmonthlymaintenance',
            name='account',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantmonthlymaintenance',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='tenantmonthlymaintenance',
            name='currency',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tenantmonthlymaintenance',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='tenantmonthlymaintenance',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]