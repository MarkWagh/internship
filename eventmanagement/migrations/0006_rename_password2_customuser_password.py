# Generated by Django 3.2.3 on 2021-05-16 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventmanagement', '0005_rename_user_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='password2',
            new_name='password',
        ),
    ]
