# Generated by Django 2.2.1 on 2019-05-24 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='meta_description',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='pages',
            name='meta_keyword',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='pages',
            name='meta_title',
            field=models.CharField(default='', max_length=250),
        ),
    ]
