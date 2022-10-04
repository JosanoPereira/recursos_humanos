# Generated by Django 4.1.1 on 2022-10-03 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0002_funcionario_departamentos_funcionario_empresa_and_more"),
        ("registrohoraextra", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="horaextra",
            name="funcionario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="funcionarios.funcionario",
            ),
            preserve_default=False,
        ),
    ]