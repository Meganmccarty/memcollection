# Generated by Django 2.2.10 on 2020-03-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_collectingtrip_states_collected'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimenrecord',
            name='unidentified',
            field=models.BooleanField(default='False', verbose_name='Is the specimen unidentified to species?'),
        ),
    ]
