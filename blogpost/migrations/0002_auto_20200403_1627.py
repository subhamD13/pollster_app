# Generated by Django 3.0.4 on 2020-04-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='published_date',
        ),
    ]
