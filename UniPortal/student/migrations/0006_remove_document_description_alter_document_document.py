# Generated by Django 4.0.4 on 2022-04-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
