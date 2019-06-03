# Generated by Django 2.2.1 on 2019-06-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bobtogether', '0003_auto_20190603_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matching',
            name='gender',
            field=models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Any')], default=1),
        ),
        migrations.AlterField(
            model_name='matching',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '모집중'), (2, '모집 완료'), (3, '만남 완료')], default=1),
        ),
    ]