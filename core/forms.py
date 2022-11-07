from django import forms
from .models import Pessoa, Produto, Servicos, Blog


class PessoaModelForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = "__all__"


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao_produto', 'preco', 'estoque']


class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servicos
        fields = ['nome_servico', 'descricao_servicos']


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title_post', 'resume_post', 'text_post', 'author']
