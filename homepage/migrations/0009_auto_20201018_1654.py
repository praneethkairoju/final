# Generated by Django 3.1.2 on 2020-10-18 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20201018_1651'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clients',
            new_name='client',
        ),
        migrations.RenameModel(
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameModel(
            old_name='services',
            new_name='service',
        ),
    ]
