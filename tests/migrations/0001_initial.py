# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.TextField(default=None)),
                ('answer2', models.TextField(default=None)),
                ('answer3', models.TextField(default=None)),
                ('answer4', models.TextField(default=None)),
                ('is_correct', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Subject')),
                ('date_publisher', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(to='tests.Question')),
            ],
            options={
                'ordering': ('date_publisher',),
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rezult', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.UserInfo'),
        ),
    ]