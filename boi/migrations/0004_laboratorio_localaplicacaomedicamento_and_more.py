# Generated by Django 5.1.3 on 2024-12-03 23:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0003_remove_boi_curral'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id_laboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='LocalAplicacaoMedicamento',
            fields=[
                ('id_localaplicacao', models.AutoField(primary_key=True, serialize=False)),
                ('local', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMedicamento',
            fields=[
                ('id_tipomedicamento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_medicamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id_medicamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('dias_carencia', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medicamento_laboratorio', to='boi.laboratorio')),
                ('local_aplicacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medicamento_local', to='boi.localaplicacaomedicamento')),
                ('tipo_medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medicamento_tipo', to='boi.tipomedicamento')),
            ],
        ),
    ]