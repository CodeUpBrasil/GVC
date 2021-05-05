from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Fornecedor, Fornecimento, Email, Telefone, Local, DadosBancarios, Servico
from .forms import FornecedorForm, EditarFornecedorForm, FornecimentoForm, EmailForm, TelefoneForm, LocalForm, DadosBancariosForm, ServicoForm

@login_required
def meus_fornecedores(request):
    context = {
        'title': 'Meus Fornecedores',
        'fornecedores': Fornecedor.objects.all()
    }
    return render(request, 'fornecedores/meus_fornecedores.html', context)

@login_required
def novo_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = FornecedorForm()

    context = {
        'title': 'Adicionar Novo Fornecedor',
        'form': form
    }

    return render(request, 'base_form_lg.html', context)

@login_required
def editar_fornecedor(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = EditarFornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = EditarFornecedorForm(instance=fornecedor)

    context = {
        'title': f"Editar fornecedor - {fornecedor.nome}",
        'form': form
    }

    return render(request, 'base_form_lg.html', context)

@login_required
def deletar_fornecedor(request, fornecedor_id):
    if request.method == 'POST':
        Fornecedor.objects.get(id=fornecedor_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novo_fornecimento(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = FornecimentoForm(request.POST)
        if form.is_valid():
            f = form.save()
            fornecedor.fornecimento.add(f)
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = FornecimentoForm()

    context = {
        'title': f'Adicionar novo fornecimento de {fornecedor.nome}',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def editar_fornecimento(request, fornecimento_id):
    try:
        fornecimento = Fornecimento.objects.get(id=fornecimento_id)
    except:
        raise Http404('Fornecimento não encontrado')

    if request.method == 'POST':
        form = FornecimentoForm(request.POST, instance=fornecimento)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = FornecimentoForm(instance=fornecimento)

    context = {
        'title': 'Editar fornecimento',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_fornecimento(request, fornecimento_id):
    if request.method == 'POST':
        Fornecimento.objects.get(id=fornecimento_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novo_email(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            f = form.save()
            fornecedor.emails.add(f)
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = EmailForm()

    context = {
        'title': f'Adicionar novo email para {fornecedor.nome}',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def editar_email(request, email_id):
    try:
        email = Email.objects.get(id=email_id)
    except:
        raise Http404('Fornecimento não encontrado')

    if request.method == 'POST':
        form = EmailForm(request.POST, instance=email)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = EmailForm(instance=email)

    context = {
        'title': 'Editar email',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_email(request, email_id):
    if request.method == 'POST':
        Email.objects.get(id=email_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novo_telefone(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = TelefoneForm(request.POST)
        if form.is_valid():
            f = form.save()
            fornecedor.telefones.add(f)
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = TelefoneForm()

    context = {
        'title': f'Adicionar novo número de Telefone para {fornecedor.nome}',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def editar_telefone(request, telefone_id):
    try:
        telefone = Telefone.objects.get(id=telefone_id)
    except:
        raise Http404('Fornecimento não encontrado')

    if request.method == 'POST':
        form = TelefoneForm(request.POST, instance=telefone)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = TelefoneForm(instance=telefone)

    context = {
        'title': 'Editar telefone',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_telefone(request, telefone_id):
    if request.method == 'POST':
        Telefone.objects.get(id=telefone_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novo_local(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            f = form.save()
            fornecedor.localizacoes.add(f)
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = LocalForm()

    context = {
        'title': f'Adicionar nova localização para {fornecedor.nome}',
        'form': form
    }

    return render(request, 'base_form_md.html', context)

@login_required
def editar_local(request, local_id):
    try:
        local = Local.objects.get(id=local_id)
    except:
        raise Http404('Fornecimento não encontrado')

    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = LocalForm(instance=local)

    context = {
        'title': 'Editar localização',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_local(request, local_id):
    if request.method == 'POST':
        Local.objects.get(id=local_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novos_dados_bancarios(request, fornecedor_id):
    try:
        fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    except:
        raise Http404('Fornecedor não encontrado')

    if request.method == 'POST':
        form = DadosBancariosForm(request.POST)
        if form.is_valid():
            f = form.save()
            fornecedor.dados_bancarios.add(f)
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = DadosBancariosForm()

    context = {
        'title': f'Adicionar novos dados bancários para {fornecedor.nome}',
        'form': form
    }

    return render(request, 'base_form_md.html', context)

@login_required
def editar_dados_bancarios(request, dados_bancarios_id):
    try:
        dados_bancarios = DadosBancarios.objects.get(id=dados_bancarios_id)
    except:
        raise Http404('Dados bancários não encontrados')

    if request.method == 'POST':
        form = DadosBancariosForm(request.POST, instance=dados_bancarios)
        if form.is_valid():
            form.save()
            return redirect('fornecedores:meus_fornecedores')
    else:
        form = DadosBancariosForm(instance=dados_bancarios)

    context = {
        'title': 'Editar dados bancários',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_dados_bancarios(request, dados_bancarios_id):
    if request.method == 'POST':
        DadosBancarios.objects.get(id=dados_bancarios_id).delete()
    return HttpResponseRedirect(reverse('fornecedores:meus_fornecedores'))

@login_required
def novo_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.POST.get('next')
            if next_url:
                return redirect(f'{next_url}')
            else:
                return redirect('fornecedores:meus_fornecedores')
    else:
        form = ServicoForm()

    context = {
        'title': f'Cadastrar novo serviço',
        'form': form
    }

    return render(request, 'fornecedores/servico_form.html', context)

@login_required
def editar_servico(request, servico_id):
    try:
        servico = Servico.objects.get(id=servico_id)
    except:
        raise Http404('Serviço não encontrado')

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            next_url = request.POST.get('next')
            if next_url:
                return redirect(f'{next_url}')
            else:
                return redirect('fornecedores:meus_fornecedores')
    else:
        form = ServicoForm(instance=servico)

    context = {
        'title': 'Editar serviço',
        'form': form
    }

    return render(request, 'base_form_sm.html', context)

@login_required
def deletar_servico(request, servico_id):
    if request.method == 'POST':
        Servico.objects.get(id=servico_id).delete()
        next_url = request.POST.get('next')
        if next_url:
            return redirect(f'{next_url}')
        else:
            return redirect('fornecedores:meus_fornecedores')
