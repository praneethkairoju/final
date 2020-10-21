# Generated by Django 3.1.2 on 2020-10-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('designation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=30)),
            ],
        ),
    ]
