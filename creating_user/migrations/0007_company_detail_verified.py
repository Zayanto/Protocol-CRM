# Generated by Django 3.0.7 on 2020-07-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creating_user', '0006_auto_20200725_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_detail',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
