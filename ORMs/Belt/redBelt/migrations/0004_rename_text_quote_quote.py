# Generated by Django 4.1.7 on 2023-03-06 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redBelt', '0003_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='text',
            new_name='quote',
        ),
    ]