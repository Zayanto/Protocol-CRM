# Generated by Django 3.0.7 on 2020-07-25 20:48

from django.db import migrations, models
import properties.models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_merge_20200721_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlymaintenance',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=properties.models.monthly_maintenance_document_file_path),
        ),
        migrations.AddField(
            model_name='tenantmonthlymaintenance',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=properties.models.monthly_maintenance_document_file_path),
        ),
    ]
