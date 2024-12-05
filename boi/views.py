from django.shortcuts import render, redirect
from django.db.models import Q
from boi import forms
from boi import models
from boi.forms import CriarCurralForm
from boi.models import Curral, Lote, Medicamento, Boi
from django.views.generic import DetailView, DeleteView, UpdateView

def home(request):
    return render(request, 'home/base.html')

def lista_curral_view(request):
    # Recupera todos os currais ordenados por nome
    currais = models.Curral.objects.all().order_by('nome')

    # Recupera o valor da busca
    search = request.GET.get('search', '').strip()

    # Se há texto na busca, filtra os currais pelo nome ou tipo de curral
    if search:
        currais = currais.filter(
            Q(nome__icontains=search) | 
            Q(curral_type__tipo_curral__icontains=search)
        )

    return render(request, 'curral/listacurral.html', {'currais': currais})

def criar_curral_view(request):
    
    if request.method == 'POST':
        criarcurral_form = forms.CriarCurralForm(request.POST)
        if criarcurral_form.is_valid():
            criarcurral_form.save()
            return redirect('criarcurral')#colocar um redirect decente dps
    else:
        criarcurral_form = forms.CriarCurralForm()

    return render(request, 'curral/criarcurral.html', {'criarcurral_form': criarcurral_form})

class CurralDetailView(DetailView):
    model = Curral
    template_name = 'curral/detalhecurral.html'
    
class CurralUpdateView(UpdateView):
    model = Curral
    form_class = CriarCurralForm
    template_name = 'curral/atualizarcurral.html'
    success_url = '/listacurral/'

class CurralDeleteView(DeleteView):
    model = Curral
    template_name = 'curral/deletarcurral.html'
    success_url = '/listacurral'





def lista_lote_view(request):
    lotes = models.Lote.objects.all().order_by('nome')

    search = request.GET.get('search', '').strip()

    if search:
        lotes = lotes.filter(
            Q(nome__icontains=search) |
            Q(curral__nome__icontains=search)
        )
    
    return render(request, 'lote/listalote.html', {'lotes': lotes})
    
def criar_lote_view(request):
    if request.method == 'POST':
        criarlote_form = forms.CriarLoteForm(request.POST)
        if criarlote_form.is_valid():
            criarlote_form.save()
            return redirect('criarlote')#colocar um redirect decente dps
    else:
        criarlote_form = forms.CriarLoteForm()

    return render(request, 'lote/criarlote.html', {'criarlote_form': criarlote_form})







def lista_boi_view(request):
    bois = models.Boi.objects.all().order_by('brinco')
    
    search = request.GET.get('search', '').strip()
    
    if search:
        # Normalize search input for comparison
        search = search.lower()
        bois = bois.filter(
            Q(brinco__icontains=search) |
            Q(fornecedor__icontains=search) |
            Q(status_boi__tipo_status__icontains=search) |
            Q(lote__nome__icontains=search) |
            Q(data_entrada__icontains=search)
        )
    
    return render(request, 'boi/listaboi.html', {'bois': bois})


def incluir_boi_view(request):
    if request.method == 'POST':
        incluirboi_form = forms.IncluirBoiForm(request.POST)
        if incluirboi_form.is_valid():
            incluirboi_form.save()
            return redirect('incluirboi')
    else:
        incluirboi_form = forms.IncluirBoiForm()
    
    return render(request, 'boi/incluirboi.html', {'incluirboi_form': incluirboi_form})








def lista_medicamento_view(request):
    medicamentos = models.Medicamento.objects.all()

    search = request.GET.get('search', '').strip()

    if search:
        search = search.lower()
        medicamentos = medicamentos.filter(
            Q(nome__icontains=search) |
            Q(laboratorio__nome__icontains=search) |
            Q(tipo_medicamento__tipo_medicamento__icontains=search) 
        )
    return render(request, 'medicamento/listamedicamento.html', {'medicamentos': medicamentos})


def criar_medicamento_view(request):
    if request.method == 'POST':
        criarmedicamento_form = forms.CriarMedicamentoForm(request.POST)
        if criarmedicamento_form.is_valid():
            criarmedicamento_form.save()
            return redirect('criarmedicamento')
    else:
        criarmedicamento_form = forms.CriarMedicamentoForm()
    
    return render(request, 'medicamento/criarmedicamento.html', {'criarmedicamento_form': criarmedicamento_form})
