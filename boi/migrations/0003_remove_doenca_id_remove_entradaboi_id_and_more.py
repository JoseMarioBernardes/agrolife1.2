# Generated by Django 5.1.3 on 2024-12-03 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0002_entradaboi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doenca',
            name='id',
        ),
        migrations.RemoveField(
            model_name='entradaboi',
            name='id',
        ),
        migrations.RemoveField(
            model_name='localaplicacaomedicamento',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lote',
            name='id',
        ),
        migrations.RemoveField(
            model_name='medicamento',
            name='id',
        ),
        migrations.RemoveField(
            model_name='pesoatualizacao',
            name='id',
        ),
        migrations.RemoveField(
            model_name='protocolo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='protocolomedicamento',
            name='id',
        ),
        migrations.RemoveField(
            model_name='protocolorealizado',
            name='id',
        ),
        migrations.RemoveField(
            model_name='raca',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sexo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='statusboi',
            name='id',
        ),
        migrations.RemoveField(
            model_name='tipomedicamento',
            name='id',
        ),
        migrations.AddField(
            model_name='doenca',
            name='id_doenca',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='entradaboi',
            name='id_entrada',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='localaplicacaomedicamento',
            name='id_localaplicacao',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='lote',
            name='id_lote',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='id_medicamento',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='pesoatualizacao',
            name='id_pesoatualizacao',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='id_protocolo',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='protocolomedicamento',
            name='id_protocolomedicamento',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='protocolorealizado',
            name='id_protocolorealizado',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='raca',
            name='id_raca',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='sexo',
            name='id_sexo',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='statusboi',
            name='id_statusboi',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='tipomedicamento',
            name='id_tipomedicamento',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boi',
            name='id_brinco',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='curral',
            name='id_curral',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doenca',
            name='nome',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='local_aplicacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boi.localaplicacaomedicamento'),
        ),
        migrations.AlterField(
            model_name='tipocurral',
            name='id_tipoCurral',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Movimentacao',
        ),
        migrations.DeleteModel(
            name='MovimentacaoGeral',
        ),
    ]