# Generated by Django 3.0.7 on 2020-07-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='owner_type',
            field=models.CharField(choices=[('investor', 'Investor'), ('normal', 'Normal')], default='normal', max_length=20, verbose_name='Type'),
        ),
    ]
