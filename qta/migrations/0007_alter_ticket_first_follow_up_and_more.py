# Generated by Django 4.2.4 on 2023-09-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qta', '0006_remove_ticket_id_ticket_id_unico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='first_follow_up',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='second_follow_up',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='third_follow_up',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
