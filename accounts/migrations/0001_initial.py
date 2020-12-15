# Generated by Django 3.1.4 on 2020-12-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personname', models.CharField(max_length=120)),
                ('accno', models.CharField(max_length=15, unique=True)),
                ('acctype', models.CharField(max_length=120)),
                ('balance', models.IntegerField(default=3000)),
                ('phonenumber', models.CharField(max_length=12, unique=True)),
                ('mpin', models.CharField(max_length=4, unique=True)),
            ],
        ),
    ]
