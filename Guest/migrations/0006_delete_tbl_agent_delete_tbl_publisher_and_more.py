# Generated by Django 5.0.3 on 2024-03-23 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_agent_tbl_publisher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_agent',
        ),
        migrations.DeleteModel(
            name='tbl_publisher',
        ),
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]