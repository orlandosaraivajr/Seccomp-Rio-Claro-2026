from django.db import models


class Contato(models.Model):
    class Categoria(models.TextChoices):
        AMIGOS = 'amigos', 'Amigos'
        FAMILIA = 'familia', 'Família'

    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=20)
    categoria = models.CharField(
        'Categoria',
        max_length=10,
        choices=Categoria.choices,
        default=Categoria.AMIGOS,
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome
