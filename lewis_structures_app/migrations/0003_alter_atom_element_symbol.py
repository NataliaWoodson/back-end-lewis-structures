# Generated by Django 4.0.6 on 2022-07-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lewis_structures_app", "0002_alter_atom_element_symbol"),
    ]

    operations = [
        migrations.AlterField(
            model_name="atom",
            name="element_symbol",
            field=models.CharField(max_length=2),
        ),
    ]
