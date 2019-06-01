# Generated by Django 2.1.7 on 2019-06-01 11:45

import annoying.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('since', models.DateTimeField(default=datetime.datetime.now)),
                ('till', models.DateTimeField(default=datetime.datetime.now)),
                ('matchingMessage', models.TextField(default='')),
                ('filter', models.TextField(default='')),
                ('maxNumber', models.PositiveIntegerField(default=2)),
                ('status', models.PositiveIntegerField(choices=[(1, 'wait for matching'), (2, 'complete recruiting'), (3, 'complete meeting')])),
            ],
        ),
        migrations.CreateModel(
            name='MatchingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestMessage', models.TextField(default='')),
                ('matching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='bobtogether.Matching')),
            ],
        ),
        migrations.CreateModel(
            name='MatchingReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(default=3)),
                ('title', models.CharField(default='', max_length=30)),
                ('detail', models.TextField(default='')),
                ('matching', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bobtogether.Matching')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('matching', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bobtogether.Matching')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('age', models.PositiveIntegerField(default=20)),
                ('school', models.CharField(default='Seoul National University', max_length=50)),
                ('major', models.CharField(default='', max_length=30)),
                ('description', models.TextField(default='')),
                ('contact', models.TextField(default='010-0000-0000')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('menu', models.TextField(default='')),
                ('location', models.TextField(default='')),
                ('hours', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='bobtogether.Profile'),
        ),
        migrations.AddField(
            model_name='matchingreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bobtogether.Profile'),
        ),
        migrations.AddField(
            model_name='matchingrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='bobtogether.Profile'),
        ),
        migrations.AddField(
            model_name='matching',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchings', to='bobtogether.Profile'),
        ),
        migrations.AddField(
            model_name='matching',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bobtogether.Restaurant'),
        ),
    ]
