# Generated by Django 4.1.2 on 2022-11-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrer',
            name='linkedin',
            field=models.CharField(default='https://linkedin.com/', max_length=150),
        ),
        migrations.AddField(
            model_name='referrer',
            name='role',
            field=models.CharField(default='sde', max_length=150),
        ),
        migrations.AddField(
            model_name='referrer',
            name='university',
            field=models.CharField(default='scu', max_length=150),
        ),
        migrations.AlterField(
            model_name='referrer',
            name='company',
            field=models.CharField(default='google', max_length=150),
        ),
    ]
