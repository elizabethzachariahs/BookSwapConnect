# Generated by Django 5.0.4 on 2024-04-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publisher', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_paddbook',
            name='pbook_price',
            field=models.IntegerField(default=0),
        ),
    ]