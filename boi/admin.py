from django.contrib import admin
from .models import (
    TipoCurral, Curral, Lote, Raca, Sexo, StatusBoi, Boi,
    PesoAtualizacao, Doenca, Protocolo, Medicamento, LocalAplicacaoMedicamento,
    TipoMedicamento, ProtocoloMedicamento, ProtocoloRealizado, EntradaBoi
)

# Registros básicos
@admin.register(TipoCurral)
class TipoCurralAdmin(admin.ModelAdmin):
    list_display = ('id_tipoCurral', 'tipo_curral')
    search_fields = ('tipo_curral',)

@admin.register(Curral)
class CurralAdmin(admin.ModelAdmin):
    list_display = ('id_curral', 'nome', 'peso_max', 'peso_min', 'capacidade_max', 'id_tipoCurral')
    search_fields = ('nome',)
    list_filter = ('id_tipoCurral',)

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('id_lote', 'nome', 'data_inicio', 'data_saida', 'curral')
    search_fields = ('nome',)
    list_filter = ('curral',)

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('id_raca', 'tipo_raca')
    search_fields = ('tipo_raca',)

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ('id_sexo', 'tipo_sexo')
    search_fields = ('tipo_sexo',)

@admin.register(StatusBoi)
class StatusBoiAdmin(admin.ModelAdmin):
    list_display = ('id_statusboi', 'tipo_status')
    search_fields = ('tipo_status',)

@admin.register(Boi)
class BoiAdmin(admin.ModelAdmin):
    list_display = ('id_brinco', 'brinco', 'fornecedor', 'raca', 'sexo', 'data_nascimento', 'data_entrada', 'peso_entrada', 'status_boi', 'lote', 'data_saida', 'peso_saida')
    search_fields = ('brinco', 'fornecedor')
    list_filter = ('raca', 'sexo', 'status_boi', 'lote')

@admin.register(PesoAtualizacao)
class PesoAtualizacaoAdmin(admin.ModelAdmin):
    list_display = ('id_pesoatualizacao', 'boi', 'novo_peso', 'data_pesagem')
    search_fields = ('boi__brinco',)
    list_filter = ('data_pesagem',)

@admin.register(Doenca)
class DoencaAdmin(admin.ModelAdmin):
    list_display = ('id_doenca', 'nome')
    search_fields = ('nome',)

@admin.register(Protocolo)
class ProtocoloAdmin(admin.ModelAdmin):
    list_display = ('id_protocolo', 'nome', 'doenca')
    search_fields = ('nome',)
    list_filter = ('doenca',)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_medicamento', 'nome', 'local_aplicacao', 'dias_carencia', 'preco', 'laboratorio', 'tipo_medicamento')
    search_fields = ('nome', 'laboratorio')
    list_filter = ('tipo_medicamento',)

@admin.register(LocalAplicacaoMedicamento)
class LocalAplicacaoMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_localaplicacao', 'local')
    search_fields = ('local',)

@admin.register(TipoMedicamento)
class TipoMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_tipomedicamento', 'tipo_medicamento')
    search_fields = ('tipo_medicamento',)

@admin.register(ProtocoloMedicamento)
class ProtocoloMedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_protocolomedicamento', 'protocolo', 'medicamento', 'dosagem')
    search_fields = ('protocolo__nome', 'medicamento__nome')

@admin.register(ProtocoloRealizado)
class ProtocoloRealizadoAdmin(admin.ModelAdmin):
    list_display = ('id_protocolorealizado', 'boi', 'protocolo_medicamento', 'data_protocolo_realizado')
    search_fields = ('boi__brinco', 'protocolo_medicamento__protocolo__nome')
    list_filter = ('data_protocolo_realizado',)

@admin.register(EntradaBoi)
class EntradaBoiAdmin(admin.ModelAdmin):
    list_display = ('id_entrada', 'descricao', 'data_criacao')
    search_fields = ('descricao',)
    list_filter = ('data_criacao',)
