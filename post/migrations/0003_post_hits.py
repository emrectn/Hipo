# Generated by Django 2.1.4 on 2018-12-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20181223_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]