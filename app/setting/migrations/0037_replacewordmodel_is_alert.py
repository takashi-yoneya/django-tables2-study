# Generated by Django 3.1.6 on 2021-05-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0036_replacewordmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='replacewordmodel',
            name='is_alert',
            field=models.BooleanField(default=False, verbose_name='アラート表示'),
        ),
    ]