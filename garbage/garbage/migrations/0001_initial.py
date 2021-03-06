# Generated by Django 3.2 on 2021-04-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MachDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField(default=0)),
                ('locate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('openId', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
                ('auth', models.IntegerField(default=0)),
                ('face', models.ImageField(upload_to='img')),
            ],
        ),
    ]
