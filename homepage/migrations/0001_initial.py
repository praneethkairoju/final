# Generated by Django 3.1.2 on 2020-10-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('servicename', models.CharField(max_length=20)),
                ('shortlist', models.BooleanField(default=False)),
            ],
        ),
    ]
