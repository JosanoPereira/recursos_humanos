# Generated by Django 4.1.1 on 2022-10-04 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0001_initial"),
        ("funcionarios", "0003_alter_funcionario_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="empresa",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="empresas.empresa",
            ),
        ),
    ]
