# Generated by Django 4.2.4 on 2023-10-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qta', '0010_ticket_time_finish'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Support_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]