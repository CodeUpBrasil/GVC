from django import forms
from django.forms import widgets
from .models import Produto, Categoria, MaterialDoProduto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    data_criacao = forms.DateField(
        input_formats=['%d/%m/%Y', '%d-%m-%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        required=False
    )
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'rounded-0 rounded-start',
                'rows': "5",
                'style': 'padding: 9px 6px;'
            }
        ),
        required=False
    )
    observacao = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': "4"}
        ),
        required=False
    )
    class Meta:
        model = Produto
        exclude = ('servicos', 'materiais')

class MaterialDoProdutoForm(forms.ModelForm):
    class Meta:
        model = MaterialDoProduto
        fields = '__all__'