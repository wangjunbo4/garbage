# Generated by Django 3.2 on 2021-04-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garbage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdb',
            name='openId2',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
