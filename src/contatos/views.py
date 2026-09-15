from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Contato
from .forms import ContatoForm


class ContatoListView(ListView):
    """Lista todos os contatos (Read)."""
    model = Contato
    template_name = 'contatos/contato_list.html'
    context_object_name = 'contatos'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.GET.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        busca = self.request.GET.get('q')
        if busca:
            queryset = queryset.filter(nome__icontains=busca)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria_atual'] = self.request.GET.get('categoria', '')
        context['busca_atual'] = self.request.GET.get('q', '')
        context['total_contatos'] = Contato.objects.count()
        context['total_amigos'] = Contato.objects.filter(categoria=Contato.Categoria.AMIGOS).count()
        context['total_familia'] = Contato.objects.filter(categoria=Contato.Categoria.FAMILIA).count()
        return context


class ContatoDetailView(DetailView):
    """Exibe os detalhes de um contato (Read)."""
    model = Contato
    template_name = 'contatos/contato_detail.html'
    context_object_name = 'contato'


class ContatoCreateView(CreateView):
    """Cria um novo contato (Create)."""
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/contato_form.html'
    success_url = reverse_lazy('contato_list')


class ContatoUpdateView(UpdateView):
    """Edita um contato existente (Update)."""
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/contato_form.html'
    success_url = reverse_lazy('contato_list')


class ContatoDeleteView(DeleteView):
    """Remove um contato (Delete)."""
    model = Contato
    template_name = 'contatos/contato_confirm_delete.html'
    success_url = reverse_lazy('contato_list')
