# Generated by Django 3.2 on 2021-06-18 19:16

from django.db import migrations, models
import mskpv.models


class Migration(migrations.Migration):

    dependencies = [
        ('mskpv', '0032_auto_20210618_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', validators=[mskpv.models.validate_image]),
        ),
    ]
