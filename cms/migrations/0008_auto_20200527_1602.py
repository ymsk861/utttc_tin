# Generated by Django 2.1.15 on 2020-05-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200525_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='photo_1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='circle',
            name='photo_2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='circle',
            name='photo_3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='circle',
            name='tag_1',
            field=models.CharField(max_length=50),
        ),
    ]
