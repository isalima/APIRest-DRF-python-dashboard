from rest_framework import serializers
from core.models import Pessoa, Produto, Blog, Servicos, FaleConosco


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = (
            'nome_pessoa',
            'cargo',
            'email',
            'cpf',
        )


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'descricao_produto',
            'preco',
            'estoque',
        )


class BlogSerializer(serializers.ModelSerializer):
    author = PessoaSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = (
            'title_post',
            'resume_post',
            'text_post',
            'author',
            'created_post',
        )
        ordering = ['created_post']


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = (
            'nome_servico',
            'descricao_servicos',
        )


class FaleConoscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaleConosco
        fields = (
            'nome_usuario',
            'mensagem',
            'email_usuario',
            'createdFaleconosco',
        )
