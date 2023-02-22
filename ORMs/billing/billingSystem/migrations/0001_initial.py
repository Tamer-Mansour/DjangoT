# Generated by Django 4.1.7 on 2023-02-22 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('class_name', models.CharField(max_length=100)),
                ('parent_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('date', models.DateField()),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.fee')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.salary')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billingSystem.student'),
        ),
    ]