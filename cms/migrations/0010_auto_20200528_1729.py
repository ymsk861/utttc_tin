# Generated by Django 2.1.15 on 2020-05-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20200528_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='mail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='circle',
            name='twitter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]