# Generated by Django 5.0.3 on 2024-04-03 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_alter_tbl_swap_frombook_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_uaddbook',
            name='ubook_genre',
        ),
        migrations.RemoveField(
            model_name='tbl_uaddbook',
            name='ubook_qlty',
        ),
        migrations.RemoveField(
            model_name='tbl_uaddbook',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_swap',
        ),
        migrations.DeleteModel(
            name='tbl_uaddbook',
        ),
    ]
