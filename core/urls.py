
from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cadastrar_pessoas/', views.PessoaAddView.as_view(), name='pessoacreat'),
    path('pessoaslist/', views.PessoaListView.as_view(), name='pessoalist'),
    path('pessoa/<int:pk>', views.DetailView.as_view(), name="pessoadetail"),
    path('updatepessoa/<int:pk>', views.PessoaUpdateView.as_view(), name="updatepessoa"),
]
