from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)  # Título do projeto
    descricao = models.TextField()  # Descrição do projeto
    imagem = models.ImageField(upload_to='projeto/imagens/')  # Imagem do projeto
    link = models.URLField(blank=True)  # Link para o projeto (opcional)
    data_criacao = models.DateField(auto_now_add=True)  # Data de criação do projeto

    def __str__(self):
        return self.titulo  # Representação do objeto como string