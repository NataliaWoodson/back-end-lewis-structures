# Generated by Django 4.0.6 on 2022-07-28 19:47
# Generated by Django 4.0.6 on 2022-07-28 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lewis_structures_app', '0013_remove_electron_paired_with'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electron',
            name='atom',
        ),
        migrations.DeleteModel(
            name='Atom',
        ),
        migrations.DeleteModel(
            name='Electron',
        ),
    ]
