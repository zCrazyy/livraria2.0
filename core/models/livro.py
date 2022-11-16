from django.db import models

from core.models import Autor, Categoria, Editora
from media.models import Image


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="livros")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return f"{self.titulo} ({self.quantidade}) - {self.preco}"

