from django.urls import reverse, reverse_lazy
from core.models import Pessoa
from core.forms import PessoaModelForm

from django.views.generic import DetailView, ListView, CreateView, UpdateView, detail, TemplateView


class IndexView(TemplateView):
    template_name = 'dashboard/index.html'


class PessoaAddView(CreateView):
    model = Pessoa
    fields = '__all__'
    template_name = "dashboard/cadastrar_pessoas.html"
    success_url = reverse_lazy('core:pessoaslist')
    context_object_name = 'addpessoa'


class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'dashboard/pessoas/pessoa_single.html'
    context_object_name = 'pessoadetail'
    pk_url_kwarg = 'pk'


class PessoaListView(ListView):
    model = Pessoa
    template_name = 'dashboard/pessoas/pessoas_list.html'
    context_object_name = 'pessoaslist'


class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = '__all__'
    template_name = 'dashboard/pessoas/editar_pessoas.html'
    context_object_name = 'updatepessoa'
    pk_url_kwarg = 'pk'

