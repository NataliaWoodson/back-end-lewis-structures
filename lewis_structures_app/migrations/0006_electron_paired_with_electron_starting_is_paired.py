# Generated by Django 4.0.6 on 2022-07-27 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "lewis_structures_app",
            "0005_alter_atom_options_electron_paired_with_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="electron",
            name="starting_is_paired",
            field=models.BooleanField(default=None),
        ),
    ]
