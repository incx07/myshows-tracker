# Generated by Django 2.2.11 on 2020-04-25 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20200413_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialcomplete',
            name='rating',
            field=models.CharField(max_length=50),
        ),
    ]
