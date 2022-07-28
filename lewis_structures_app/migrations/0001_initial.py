# Generated by Django 4.0.6 on 2022-07-23 17:08

# from lewis_structures_backend import CASCADE
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Atom",
            fields=[
                ("atom_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("element_symbol", models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name="Molecule",
            fields=[
                ("molecule_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("molecular_formula", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Electron",
            fields=[
                ("electron_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("is_paired", models.BooleanField(default=False)),
                # ('atom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lewis_structures_app.atom')),
            ],
        ),
        migrations.AddField(
            model_name="atom",
            name="molecule",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="lewis_structures_app.molecule",
            ),
        ),
        migrations.AddField(
            model_name="electron",
            name="atom",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="lewis_structures_app.atom",
            ),
        ),
    ]
