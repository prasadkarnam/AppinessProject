# Generated by Django 2.2.3 on 2019-07-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20190727_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='appinessurl',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
