# Generated by Django 2.2.11 on 2021-07-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20210710_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialcomplete',
            name='myshows_id',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='seriallater',
            name='myshows_id',
            field=models.PositiveSmallIntegerField(default=0, unique=True),
        ),
    ]