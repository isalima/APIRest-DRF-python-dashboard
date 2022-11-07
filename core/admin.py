from django.contrib import admin
from .models import Pessoa, Produto, Servicos, Blog

admin.site.register(Produto)
admin.site.register(Pessoa)
admin.site.register(Servicos)
admin.site.register(Blog)


