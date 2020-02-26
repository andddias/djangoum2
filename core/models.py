from django.db import models

from django.contrib.auth.models import User


# Forma 1 - Não é a ideal
# Criação de classe de postagem usando usuario importado Django
class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo


from django.conf import settings


# Forma 2 - Ainda Não ideal
# Criação de classe de postagem usando usuario importado Django
class Post(models.Model):
    autor = models.ForeignKey(settings.AUTO_USER_MODEL, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
