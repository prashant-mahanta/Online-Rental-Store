# Generated by Django 2.1.2 on 2018-11-06 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ors', '0009_merge_20181106_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='name',
        ),
    ]