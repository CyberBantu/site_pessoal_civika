from django.views.generic import ListView
from .models import Projeto

class ListaProjetos(ListView):
    model = Projeto  # Modelo usado na view
    template_name = 'lista_projetos.html'  # Template usado para renderizar a view
    context_object_name = 'projetos'  # Nome da variável no template