# Generated by Django 4.0.5 on 2022-07-02 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_first', '0002_remove_blogpost_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='text',
        ),
    ]
