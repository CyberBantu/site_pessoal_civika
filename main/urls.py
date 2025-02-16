from django.contrib import admin
from django.urls import path
from projeto.views import ListaProjetos
from blog.views import ListaPosts, DetalhePost, CriarPost, AtualizarPost, DeletarPost
from accounts.views import register_view, login_view, logout_view # importando a função register_view em accounts/views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projeto/', ListaProjetos.as_view(), name='lista_projetos'),
    path('blog/', ListaPosts.as_view(), name='lista_posts'),
    path('blog/<slug:slug>/', DetalhePost.as_view(), name='detalhe_post'),
    path('register/', register_view, name='register'), # Adicionando a rota register
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name = 'logout'),
    path('criar/', CriarPost.as_view(), name='criar_post'),  # Criar um post
    path('<slug:slug>/atualizar/', AtualizarPost.as_view(), name='atualizar_post'),  # Atualizar um post
    path('<slug:slug>/deletar/', DeletarPost.as_view(), name='deletar_post'),  # Deletar um post
]