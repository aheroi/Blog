# Generated by Django 4.0.5 on 2022-07-02 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_first', '0005_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'blogs'},
        ),
    ]
