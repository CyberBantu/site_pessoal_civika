from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')  # Campos exibidos na lista de projetos
    search_fields = ('titulo',)  # Campos pesquisáveis