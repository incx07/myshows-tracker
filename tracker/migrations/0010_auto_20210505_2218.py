# Generated by Django 2.2.21 on 2021-05-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20200614_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialcomplete',
            name='rating',
            field=models.CharField(default='No', max_length=50),
        ),
    ]
