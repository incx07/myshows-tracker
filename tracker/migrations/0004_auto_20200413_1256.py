# Generated by Django 2.2.11 on 2020-04-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200413_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='serialcomplete',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='serialcomplete',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seriallater',
            name='year',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
