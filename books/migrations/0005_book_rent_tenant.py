# Generated by Django 3.0.1 on 2020-06-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200619_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rent_tenant',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]