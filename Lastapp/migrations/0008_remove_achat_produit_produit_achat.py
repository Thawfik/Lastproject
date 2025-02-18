# Generated by Django 5.1.3 on 2025-02-18 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Lastapp", "0007_alter_achat_statut"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="achat",
            name="Produit",
        ),
        migrations.AddField(
            model_name="produit",
            name="Achat",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Lastapp.achat",
            ),
        ),
    ]
