# Generated by Django 2.1.7 on 2019-06-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bobtogether', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matching',
            name='gender',
            field=models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Any')], default=3),
        ),
    ]
