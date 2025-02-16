from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')  # Campos exibidos na lista de posts
    prepopulated_fields = {'slug': ('titulo',)}  # Gera o slug automaticamente com base no título