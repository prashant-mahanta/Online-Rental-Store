# Generated by Django 2.1.2 on 2018-11-06 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ors', '0006_auto_20181102_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requestseller',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requestseller',
            name='status',
            field=models.CharField(choices=[('requested', 'requested'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='requested', max_length=20),
        ),
    ]