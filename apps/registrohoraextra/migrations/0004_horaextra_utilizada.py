# Generated by Django 4.1.1 on 2022-10-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrohoraextra", "0003_horaextra_horas"),
    ]

    operations = [
        migrations.AddField(
            model_name="horaextra",
            name="utilizada",
            field=models.BooleanField(default=False),
        ),
    ]