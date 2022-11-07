from django.db import models
from django.contrib.auth.models import User

# from ckeditor_uploader.fields import RichTextUploadingField


class Pessoa(models.Model):
    nome_pessoa = models.CharField('nome_pessoa', max_length=500, default='Nome')
    cpf = models.CharField('cpf', max_length=11, default='Cpf')
    cargo = models.CharField('cargo', max_length=50, default='Cargo')
    email = models.EmailField('email', max_length=50)

    # img-pessoa = Aqui fica uma imagem para a pessoa

    def __str__(self):
        return self.nome_pessoa


class Produto(models.Model):
    descricao_produto = models.CharField(max_length=200, default='Breve descricao produto')
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    estoque = models.IntegerField('quantidade em estoque')

    #   img-produto = imagem para o produto

    def __str__(self):
        return self.descricao_produto


class Blog(models.Model):
    title_post = models.CharField(max_length=100, default='Título')
    resume_post = models.CharField(max_length=100, default='resumo')
    text_post = models.CharField(max_length=500, default='Texto')
    created_post = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    # Aqui deve ter uma variavel de imagem para o post

    def __str__(self):
        return self.title_post


class Servicos(models.Model):
    nome_servico = models.CharField(max_length=15)
    descricao_servicos = models.CharField(max_length=200)

    # img-servico = imagem para servico

    def __str__(self):
        return self.nome_servico


class FaleConosco(models.Model):
    nome_usuario = models.CharField(max_length=25)
    mensagem = models.CharField(max_length=100)
    email_usuario = models.EmailField('e-mail', max_length=50)
    createdFaleconosco = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_usuario
