# Generated by Django 4.0.5 on 2022-07-02 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_first', '0004_blogpost_title_alter_blogpost_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'entries'},
        ),
    ]
