# Generated by Django 2.2.3 on 2019-07-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0015_delete_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='page_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pages',
            name='page_author',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pages',
            name='page_parent',
            field=models.IntegerField(default=0),
        ),
    ]