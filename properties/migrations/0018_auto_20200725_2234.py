# Generated by Django 3.0.7 on 2020-07-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20200725_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlymaintenance',
            name='account',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='monthlymaintenance',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='monthlymaintenance',
            name='currency',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='monthlymaintenance',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
