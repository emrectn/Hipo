# Generated by Django 2.1.4 on 2018-12-25 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_search_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PreviousSearches',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Search Titles'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]