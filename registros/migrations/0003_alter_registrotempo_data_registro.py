# Generated by Django 5.1.2 on 2024-10-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_registrotempo_horas_trabalhadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrotempo',
            name='data_registro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
