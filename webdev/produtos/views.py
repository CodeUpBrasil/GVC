from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from .models import Produto, Categoria
from .forms import ProdutoForm, CategoriaForm
from django.contrib.auth.decorators import login_required

@login_required
def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:estoque_produtos')
    else:
        form = ProdutoForm()

    context = {
        'title': 'Adicionar Novo Produto',
        'form': form
    }

    return render(request, 'base_form_lg.html', context)

@login_required
def editar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except:
        raise Http404('Produto não encontrado')

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:estoque_produtos')
    else:
        form = ProdutoForm(instance=produto)

    context = {
        'title': 'Editar Produto',
        'form': form
    }

    return render(request, 'base_form_lg.html', context)

@login_required
def deletar_produto(request, produto_id):
    if request.method == 'POST':
        Produto.objects.get(id=produto_id).delete()
    return HttpResponseRedirect(reverse('produtos:estoque_produtos'))

@login_required
def estoque(request):
    context = {
        'title': 'Estoque de Produtos',
        'produtos': Produto.objects.all()
    }
    return render(request, 'produtos/estoque_produtos.html', context)