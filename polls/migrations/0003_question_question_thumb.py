# Generated by Django 2.2 on 2019-04-18 08:42

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_thumb',
            field=s3direct.fields.S3DirectField(default='null.png'),
        ),
    ]