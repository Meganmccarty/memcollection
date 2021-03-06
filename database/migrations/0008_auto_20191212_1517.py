# Generated by Django 2.2.6 on 2019-12-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20191117_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimenrecord',
            name='collector',
            field=models.ManyToManyField(blank=True, help_text='Enter the name of the specimen collector(s).', to='database.Collector', verbose_name='Collector(s)'),
        ),
    ]
