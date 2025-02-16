from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from blog.form import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin  # Adicione esta linha


# Lista de posts
class ListaPosts(ListView):
    model = Post
    template_name = 'lista_posts.html'
    context_object_name = 'posts'

# Detalhes de um post
class DetalhePost(DetailView):
    model = Post
    template_name = 'detalhe_post.html'
    context_object_name = 'post'

# Criar um novo post
class CriarPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'criar_post.html'
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Define o autor como o usuário logado
        return super().form_valid(form)
    
    
# Atualizar um post
class AtualizarPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'atualizar_post.html'
    success_url = reverse_lazy('lista_posts')  # Redireciona após a atualização

# Deletar um post
class DeletarPost(DeleteView):
    model = Post
    template_name = 'deletar_post.html'
    success_url = reverse_lazy('lista_posts')  # Redireciona após a exclusão