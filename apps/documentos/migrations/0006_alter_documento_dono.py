# Generated by Django 4.1.1 on 2022-10-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0004_alter_funcionario_empresa"),
        ("documentos", "0005_alter_documento_dono"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documento",
            name="dono",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="funcionarios.funcionario",
                verbose_name="Proprietário do Documento",
            ),
        ),
    ]
