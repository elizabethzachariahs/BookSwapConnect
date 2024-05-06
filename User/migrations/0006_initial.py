# Generated by Django 5.0.3 on 2024-04-02 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_tbl_quality'),
        ('Guest', '0009_tbl_agent_tbl_publisher'),
        ('User', '0005_remove_tbl_uaddbook_ubook_genre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_uaddbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubook_name', models.CharField(max_length=15)),
                ('ubook_desc', models.CharField(max_length=50)),
                ('ubook_price', models.EmailField(max_length=50)),
                ('ubook_photo', models.FileField(upload_to='Assets/UserBookPhoto/')),
                ('ubook_authname', models.CharField(max_length=15)),
                ('ubook_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_genre')),
                ('ubook_qlty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_quality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_swap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swap_id', models.CharField(max_length=15)),
                ('swap_status', models.CharField(max_length=15)),
                ('swap_price', models.CharField(max_length=15)),
                ('swap_paymentstatus', models.CharField(max_length=15)),
                ('fromuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromuser_id', to='Guest.tbl_user')),
                ('touser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touser_id', to='Guest.tbl_user')),
                ('frombook_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frombook_id', to='User.tbl_uaddbook')),
                ('tobook_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tobook_id', to='User.tbl_uaddbook')),
            ],
        ),
    ]