# Generated by Django 4.1.7 on 2023-03-03 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TheUsers', '0005_user_email_verification_code_user_is_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_verification_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_email_verified',
        ),
    ]
