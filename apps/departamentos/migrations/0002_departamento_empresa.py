# Generated by Django 4.1.1 on 2022-10-06 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0001_initial"),
        ("departamentos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="departamento",
            name="empresa",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="empresas.empresa",
            ),
            preserve_default=False,
        ),
    ]
