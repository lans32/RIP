# Generated by Django 4.2.4 on 2024-10-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_askoperation_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='askoperation',
            name='result',
            field=models.BooleanField(default=None, null=True),
        ),
    ]