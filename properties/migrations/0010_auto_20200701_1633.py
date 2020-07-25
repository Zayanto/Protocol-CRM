# Generated by Django 3.0.7 on 2020-07-01 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20200630_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='stagebuying',
            name='properties',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage_buying', to='properties.Property'),
        ),
        migrations.AddField(
            model_name='stageopportunity',
            name='properties',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stage_opportunity', to='properties.Property'),
        ),
    ]
