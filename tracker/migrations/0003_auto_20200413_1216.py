# Generated by Django 2.2.11 on 2020-04-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20200409_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='SerialComplete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_eng', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Serial',
            new_name='SerialLater',
        ),
    ]
