# Generated by Django 2.2.6 on 2019-11-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_collectingtripimage_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mona',
            name='mona',
            field=models.DecimalField(decimal_places=2, help_text='Enter the MONA (Hodges) # for a species (Lepidoptera only).', max_digits=8),
        ),
    ]
