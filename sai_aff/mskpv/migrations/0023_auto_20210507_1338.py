# Generated by Django 3.2 on 2021-05-07 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mskpv', '0022_auto_20210507_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='---', max_length=225),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=225),
        ),
    ]
