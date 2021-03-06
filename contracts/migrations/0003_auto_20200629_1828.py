# Generated by Django 3.0.7 on 2020-06-29 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_remove_property_location'),
        ('contracts', '0002_auto_20200622_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20, verbose_name='Payment Status'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('inactive', 'Inactive')], default='active', max_length=20, verbose_name='Status'),
        ),
    ]
