# Generated by Django 4.2.4 on 2024-10-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ask',
            name='first_operand',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='askoperation',
            name='second_operand',
            field=models.BooleanField(default=False),
        ),
    ]