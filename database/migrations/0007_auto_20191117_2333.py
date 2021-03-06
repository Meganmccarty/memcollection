# Generated by Django 2.2.6 on 2019-11-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20191110_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='preparation',
            field=models.CharField(blank=True, choices=[('Spread', 'Spread'), ('Pinned', 'Pinned'), ('Minuten', 'Minuten'), ('Pointed', 'Pointed'), ('Envelope.', 'Envelope'), ('Container', 'Container'), ('Alcohol', 'Alcohol')], default='', help_text='Select the method with which the specimen was prepared.', max_length=20),
        ),
    ]
