# Generated by Django 3.0.5 on 2021-05-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0010_event_eventcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pincode',
            field=models.IntegerField(default=''),
        ),
    ]