# Generated by Django 4.1.7 on 2023-03-13 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_request_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='user_id',
            new_name='person',
        ),
    ]