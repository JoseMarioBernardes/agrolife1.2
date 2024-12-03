from django.shortcuts import render, redirect, get_object_or_404
from .models import Boi, Raca, Sexo, Lote, Curral, StatusBoi, EntradaBoi, TipoCurral
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction



def home(request):
    return render(request, 'home/base.html')


def incluirboi(request):
    if request.method == 'POST':
        # Debugging: Log POST data
        print("Received POST data:", request.POST)

        # Capture form data
        brinco = request.POST.get('brinco', '').strip()
        fornecedor = request.POST.get('fornecedor', '').strip()
        id_sexo = request.POST.get('sexo', '').strip()
        id_raca = request.POST.get('raca', '').strip()
        id_lote = request.POST.get('lote', '').strip()
        peso_entrada = request.POST.get('peso', '').strip()
        data_entrada = request.POST.get('dataEntrada', '').strip()
        data_nascimento = request.POST.get('dataNascimento', '').strip()

        # Validate inputs
        missing_fields = []
        if not brinco:
            missing_fields.append("Brinco")
        if not fornecedor:
            missing_fields.append("Fornecedor")
        if not id_sexo:
            missing_fields.append("Sexo")
        if not id_raca:
            missing_fields.append("Raça")
        if not id_lote:
            missing_fields.append("Lote")
        if not peso_entrada:
            missing_fields.append("Peso Entrada")
        if not data_entrada:
            missing_fields.append("Data Entrada")
        if not data_nascimento:
            missing_fields.append("Data Nascimento")

        if missing_fields:
            messages.error(request, f"Os seguintes campos são obrigatórios: {', '.join(missing_fields)}")
            return redirect('incluirboi')

        try:
            # Fetch related objects
            status_boi = StatusBoi.objects.get(id_statusboi=1)
            sexo = Sexo.objects.get(id_sexo=id_sexo)
            raca = Raca.objects.get(id_raca=id_raca)
            lote = Lote.objects.get(id_lote=id_lote)

            # Save new Boi object
            boi = Boi(
                brinco=brinco,
                fornecedor=fornecedor,
                sexo=sexo,
                raca=raca,
                lote=lote,
                data_nascimento=data_nascimento,
                data_entrada=data_entrada,
                peso_entrada=peso_entrada,
                status_boi=status_boi
            )
            boi.save()
            messages.success(request, "Animal incluído com sucesso!")
            return redirect('incluirboi')
        except Sexo.DoesNotExist:
            messages.error(request, "Sexo selecionado é inválido.")
        except Raca.DoesNotExist:
            messages.error(request, "Raça selecionada é inválida.")
        except Lote.DoesNotExist:
            messages.error(request, "Lote selecionado é inválido.")
        except Exception as e:
            messages.error(request, f"Ocorreu um erro ao incluir o animal: {e}")
        
        return redirect('incluirboi')

    else:
        # Prepare form options
        racas = Raca.objects.all()
        sexos = Sexo.objects.all()
        lotes = Lote.objects.all()

        context = {
            'racas': racas,
            'sexos': sexos,
            'lotes': lotes,
        }
        return render(request, 'boi/incluirboi.html', context)

def editarboi(request, brinco):
    # Busca o boi pelo brinco
    boi = get_object_or_404(Boi, brinco=brinco)
    sexos = Sexo.objects.all()
    racas = Raca.objects.all()
    lotes = Lote.objects.all()

    if request.method == 'POST':
        try:
            # Atualiza os campos do boi com validações
            boi.sexo_id = request.POST.get('sexo') or None
            boi.data_nascimento = request.POST.get('dataNascimento') or None
            boi.raca_id = request.POST.get('raca') or None

            lote_id = request.POST.get('lote')
            if not lote_id:
                raise ValueError("O campo 'lote' é obrigatório.")
            boi.lote_id = lote_id

            peso = request.POST.get('peso')
            if not peso or float(peso) <= 0:
                raise ValueError("O peso deve ser maior que zero.")
            boi.peso_entrada = peso

            boi.save()
            messages.success(request, 'Animal atualizado com sucesso!')
            return redirect('consultarboi')
        except Exception as e:
            messages.error(request, f'Erro ao atualizar animal: {e}')

    # Renderiza a página de edição com o contexto necessário
    context = {
        'boi': boi,
        'sexos': sexos,
        'racas': racas,
        'lotes': lotes,
    }
    return render(request, 'boi/editarboi.html', context)

def consultarboi(request):
    if request.method == 'POST':
        # Retrieve the selected brinco from the form data
        selected_brinco = request.POST.get('selectedAnimal')
        if selected_brinco:
            # Redirect to the editarboi page for the selected animal
            return redirect('editarboi', brinco=selected_brinco)
        else:
            # Display a message if no animal was selected
            messages.error(request, "Por favor, selecione um animal para editar.")

    # Default behavior for GET request
    query = request.GET.get('q', '')  # Obter termo de busca
    if query:
        bois = Boi.objects.filter(brinco__icontains=query)  # Filtrar por 'brinco'
    else:
        bois = Boi.objects.all()
    return render(request, 'boi/consultarboi.html', {'bois': bois, 'query': query})

def consultar_curral(request):
    query = request.GET.get('q', '')  # Termo de busca
    if query:
        currais = Curral.objects.filter(nome__icontains=query)
    else:
        currais = Curral.objects.all()
    return render(request, 'curral/consultar_curral.html', {'currais': currais, 'query': query})

# Editar Curral
def editar_curral(request, id_curral):
    # Recupera o curral ou retorna 404 se não encontrado
    curral = get_object_or_404(Curral, id_curral=id_curral)
    
    if request.method == 'POST':
        try:
            # Captura dados do formulário
            nome = request.POST.get('nome')
            peso_min = request.POST.get('peso_min')
            peso_max = request.POST.get('peso_max')
            capacidade_max = request.POST.get('capacidade_max')
            tipo_curral_id = request.POST.get('tipo_curral')

            # Validações básicas
            if not nome or not peso_min or not peso_max or not capacidade_max or not tipo_curral_id:
                raise ValueError("Todos os campos são obrigatórios.")
            
            # Atualiza os dados do curral
            curral.nome = nome
            curral.peso_min = peso_min
            curral.peso_max = peso_max
            curral.capacidade_max = capacidade_max
            curral.id_tipoCurral = TipoCurral.objects.get(id_tipoCurral=tipo_curral_id)

            curral.save()
            messages.success(request, "Curral editado com sucesso!")
            return redirect('consultarcurral')

        except TipoCurral.DoesNotExist:
            messages.error(request, "Tipo de curral inválido.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Erro inesperado: {e}")
    
    # Recupera tipos de curral disponíveis para o formulário
    tipos_currais = TipoCurral.objects.all()
    return render(request, 'curral/editar_curral.html', {'curral': curral, 'tipos_currais': tipos_currais})

# Excluir Currais
def excluir_currais(request):
    if request.method == 'POST':
        ids = request.POST.getlist('selected_currais')
        try:
            Curral.objects.filter(id_curral__in=ids).delete()
            messages.success(request, f"{len(ids)} curral(is) excluído(s) com sucesso!")
        except Exception as e:
            messages.error(request, f"Erro ao excluir curral(is): {e}")
    return redirect('consultarcurral')


def criar_curral(request):
    if request.method == 'POST':
        try:
            # Captura os dados enviados no formulário
            nome = request.POST['nome']
            peso_min = request.POST['peso_min']
            peso_max = request.POST['peso_max']
            capacidade_max = request.POST['capacidade_max']
            tipo_curral_id = request.POST['tipo_curral']

            # Validações básicas
            if not nome or not peso_min or not peso_max or not capacidade_max or not tipo_curral_id:
                raise ValueError("Todos os campos são obrigatórios.")

            # Valida se o tipo de curral existe
            tipo_curral = TipoCurral.objects.get(id_tipoCurral=tipo_curral_id)

            # Criação do curral
            Curral.objects.create(
                nome=nome,
                peso_min=peso_min,
                peso_max=peso_max,
                capacidade_max=capacidade_max,
                id_tipoCurral=tipo_curral
            )
            messages.success(request, "Curral criado com sucesso!")
            return redirect('consultarcurral')
        except TipoCurral.DoesNotExist:
            messages.error(request, "Tipo de curral inválido.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"Erro inesperado: {e}")
    
    # Recupera tipos de curral disponíveis
    tipos_currais = TipoCurral.objects.all()
    return render(request, 'curral/criar_curral.html', {'tipos_currais': tipos_currais})