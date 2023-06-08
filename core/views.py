from django.shortcuts import render, redirect
from core.forms import *
from core.models import *
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'

@login_required
def cadastro_cliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso')
            return redirect('url_listagem_clientes')
        contexto = {'form': form, 'txt_title':'cad_cli', 'txt_descricao':'Cadastro de Cliente', 'txt_button':'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')

@login_required
def listagem_clientes(request):
    if request.POST and request.POST['input_pesquisa']:
        dados = Cliente.objects.filter(nome__contains=request.POST['input_pesquisa'])
    else:
        dados = Cliente.objects.all()
    contexto = {'dados': dados , 'txt':"digite o nome do cliente", 'listagem':True}
    return render(request, 'core/listagem_clientes.html',contexto)


@login_required
def cadastro_veiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_veiculos')
        contexto = {'form':form, 'txt_title':'cad_veic', 'txt_descricao':'Cadastro de Veículo', 'txt_button':'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


@login_required
def listagem_veiculos(request):
    if request.user.is_staff:
        dados = Veiculo.objects.all()
        contexto = {'dados': dados,'listagem':True}
        return render(request,'core/listagem_veiculos.html', contexto)
    return render(request, 'core/mensagem.html')


@login_required()
def atualiza_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso')
            return redirect('url_listagem_clientes')
        contexto = {'form': form, 'txt_title':'atualizaCliente', 'txt_descricao':'Atualiza Cliente', 'txt_button':'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/mensagem.html')


@login_required()
def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        contexto = {'txt_msg': obj.nome, 'txt_url':'/listagem_clientes/'}
        if request.POST:
            obj.delete()
            messages.success(request, 'Cliente excluido com sucesso')
            contexto.update({'txt_tipo':'Cliente'})
            return render(request, 'core/mensagem_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html',contexto)
    return render(request, 'core/mensagem.html')


def atualiza_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    contexto = {'form': form, 'txt_title':'atualizaVeiculo', 'txt_descricao':'Atualiza Veiculo', 'txt_button':'Atualizar'}
    return render(request, 'core/cadastro.html', contexto)


def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    obj.delete()
    return redirect('url_listagem_veiculos')


def cadastro_tabela(request):
    pass


def listagem_tabelas(request):
    pass


def altera_tabela(request, id):
    pass


def exclui_tabela(request, id):
    pass


def cadastro_rotativo(request):
    form = FormRotativo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem_rotativos')
    else:
        contexto = {'form':form, 'txt_title':'cadRot', 'txt_descricao':'Cadastro de Rotativo', 'txt_button':'Cadastrar'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)


def listagem_rotativos(request):
    dados = Rotativo.objects.all()
    contexto = {'dados':dados, 'listagem':True}
    return render(request, 'core/listagem_rotativos.html', contexto)


def atualiza_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    form = FormRotativo(request.POST or None, instance=obj)
    if form.is_valid():
        obj.calcula_total()
        form.save()
        return redirect('url_listagem_rotativos')
    else:
        contexto = {'form':form, 'txt_title':'EditRot', 'txt_descricao':'Atualiza Rotativo', 'txt_button':'Salvar'}
        return render(request, 'core/cadastro.html', contexto)



def exclui_rotativo(request, id):
    pass