# Generated by Django 4.0.5 on 2022-07-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='text',
        ),
    ]
