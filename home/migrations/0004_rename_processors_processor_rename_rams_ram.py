# Generated by Django 4.1.2 on 2022-10-30 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gpu_hdd_mobo_ssd'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Processors',
            new_name='Processor',
        ),
        migrations.RenameModel(
            old_name='Rams',
            new_name='Ram',
        ),
    ]
