# Generated by Django 2.1.15 on 2020-05-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_user_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0)),
                ('circle', models.IntegerField(default=0)),
            ],
        ),
    ]
