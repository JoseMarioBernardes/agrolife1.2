from django import forms
from boi import models
from django.forms.widgets import DateInput

# class CriarCurralForm(forms.Form):
#     nome = forms.CharField(max_length=45)
#     peso_min = forms.DecimalField(max_digits=10, decimal_places=2)
#     peso_max = forms.DecimalField(max_digits=10, decimal_places=2)
#     capacidade_max = forms.IntegerField()
#     curral_type = forms.ModelChoiceField(models.TipoCurral.objects.all())

class CriarCurralForm(forms.ModelForm):
    
    class Meta:
        model = models.Curral
        fields = '__all__'


# class CriarLoteForm(forms.ModelForm):

#     class Meta:
#         model = models.Lote
#         fields = '__all__'

class CriarLoteForm(forms.Form):
    nome = forms.CharField(max_length=20)
    data_incio = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    curral = forms.ModelChoiceField(models.Curral.objects.all())

    def save(self):
        lote = models.Lote(
            nome = self.cleaned_data['nome'],
            data_inicio = self.cleaned_data['data_inicio'],
            curral = self.cleaned_data['curral']
        )
        lote.save()
        return lote


class IncluirBoiForm(forms.Form):
    brinco = forms.CharField(max_length=45)
    fornecedor = forms.CharField(max_length=50)
    raca = forms.ModelChoiceField(models.Raca.objects.all())
    sexo = forms.ModelChoiceField(models.Sexo.objects.all())
    peso_entrada = forms.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    data_entrada = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    status_boi = forms.ModelChoiceField(models.StatusBoi.objects.all())
    lote = forms.ModelChoiceField(models.Lote.objects.all())
    
    def save(self):
        boi = models.Boi(
            brinco=self.cleaned_data['brinco'],
            fornecedor=self.cleaned_data['fornecedor'],  # Corrigido o typo "forncedor"
            raca=self.cleaned_data['raca'],
            sexo=self.cleaned_data['sexo'],
            peso_entrada=self.cleaned_data['peso_entrada'],
            peso_saida=self.cleaned_data.get('peso_saida'),  # Usa get para campos opcionais
            data_nascimento=self.cleaned_data['data_nascimento'],
            data_entrada=self.cleaned_data['data_entrada'],
            data_saida=self.cleaned_data.get('data_saida'),  # Usa get para campos opcionais
            status_boi=self.cleaned_data['status_boi'],
            lote=self.cleaned_data['lote'],
        )
        boi.save()  # Salva a instância no banco de dados
        return boi  # Retorna a instância salva
    


class CriarMedicamentoForm(forms.ModelForm):
    
    class Meta:
        model = models.Medicamento
        fields = '__all__'

