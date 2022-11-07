from rest_framework.generics import get_object_or_404

from core.models import Servicos, Produto, FaleConosco, Blog, Pessoa
from core_api.serializers import PessoaSerializer
from rest_framework import generics, viewsets, permissions


class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


"""

class ServicosViewSet(viewsets.ModelViewSet):
   
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ----------------------------------------------------------
class ProdutoViewSet(viewsets.ModelViewSet):
  
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# --------------------------------------------------------
class FaleConoscoViewSet(viewsets.ModelViewSet):

    queryset = FaleConosco.objects.all()
    serializer_class = FaleConoscoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# -----------------------------------------------------------
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
"""
