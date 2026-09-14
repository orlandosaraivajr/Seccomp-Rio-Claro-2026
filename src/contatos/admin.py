from django.contrib import admin

from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome', 'telefone')
