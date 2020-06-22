# Generated by Django 3.0.1 on 2020-06-22 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=2000, null=True)),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('unpaid', 'Unpaid'), ('sent', 'Sent'), ('paid', 'Paid')], default='unpaid', max_length=20, verbose_name='Status')),
                ('invoice_start_date', models.DateTimeField(blank=True, null=True)),
                ('invoice_end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]