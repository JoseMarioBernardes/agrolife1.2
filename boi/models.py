from django.db import models

# Modelo para Tipo_currral
class TipoCurral(models.Model):
    id_tipoCurral = models.AutoField(primary_key=True)
    tipo_curral = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_curral


# Modelo para Curral
class Curral(models.Model):
    id_curral = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    peso_max = models.DecimalField(max_digits=10, decimal_places=2)
    peso_min = models.DecimalField(max_digits=10, decimal_places=2)
    capacidade_max = models.IntegerField()
    id_tipoCurral = models.ForeignKey(TipoCurral, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Modelo para Lote
class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    data_inicio = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    curral = models.ForeignKey(Curral, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Modelo para Raca
class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)
    tipo_raca = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_raca


# Modelo para Sexo
class Sexo(models.Model):
    id_sexo = models.AutoField(primary_key=True)
    tipo_sexo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_sexo


# Modelo para Status_boi
class StatusBoi(models.Model):
    id_statusboi= models.AutoField(primary_key=True)
    tipo_status = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo_status


# Modelo para Boi
class Boi(models.Model):
    id_brinco = models.AutoField(primary_key=True)
    brinco = models.CharField(max_length=15)    
    fornecedor = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    peso_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    status_boi = models.ForeignKey(StatusBoi, on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    data_saida = models.DateField(null=True, blank=True)
    peso_saida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Boi {self.brinco} - {self.raca}"


# Modelo para Peso_atualizacao
class PesoAtualizacao(models.Model):
    id_pesoatualizacao = models.AutoField(primary_key=True)
    boi = models.ForeignKey(Boi, on_delete=models.CASCADE)
    novo_peso = models.DecimalField(max_digits=10, decimal_places=2)
    data_pesagem = models.DateField()

    def __str__(self):
        return f"Peso do Boi {self.boi.cod_branco} atualizado para {self.novo_peso}"


# Modelo para Doenca
class Doenca(models.Model):
    id_doenca = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome


# Modelo para Protocolo
class Protocolo(models.Model):
    id_protocolo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Modelo para Medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    local_aplicacao = models.ForeignKey('LocalAplicacaoMedicamento', on_delete=models.CASCADE, default=1)
    dias_carencia = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    laboratorio = models.CharField(max_length=30)
    tipo_medicamento = models.ForeignKey('TipoMedicamento', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Modelo para Local_aplicacao_medicamento
class LocalAplicacaoMedicamento(models.Model):
    id_localaplicacao = models.AutoField(primary_key=True)
    local = models.CharField(max_length=20)

    def __str__(self):
        return self.local


# Modelo para Tipo_medicamento
class TipoMedicamento(models.Model):
    id_tipomedicamento = models.AutoField(primary_key=True)
    tipo_medicamento = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_medicamento


# Modelo para Protocolo_medicamento
class ProtocoloMedicamento(models.Model):
    id_protocolomedicamento = models.AutoField(primary_key=True)
    protocolo = models.ForeignKey(Protocolo, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosagem = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Protocolo: {self.protocolo} - Medicamento: {self.medicamento}"


# Modelo para Protocolo_realizado
class ProtocoloRealizado(models.Model):
    id_protocolorealizado = models.AutoField(primary_key=True)
    boi = models.ForeignKey(Boi, on_delete=models.CASCADE)
    protocolo_medicamento = models.ForeignKey(ProtocoloMedicamento, on_delete=models.CASCADE)
    data_protocolo_realizado = models.DateField()

    def __str__(self):
        return f"Protocolo Realizado para Boi {self.boi.cod_branco} em {self.data_protocolo_realizado}"

class EntradaBoi(models.Model):
    id_entrada = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=255, default="Nova entrada")
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Entrada #{self.id} - {self.descricao}"