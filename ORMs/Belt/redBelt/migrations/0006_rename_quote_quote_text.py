# Generated by Django 4.1.7 on 2023-03-06 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redBelt', '0005_rename_user_quote_addby_quote_favourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='quote',
            new_name='text',
        ),
    ]