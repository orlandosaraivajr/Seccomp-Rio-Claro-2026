from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='contato_list'),
    path('contatos/novo/', views.ContatoCreateView.as_view(), name='contato_create'),
    path('contatos/<int:pk>/', views.ContatoDetailView.as_view(), name='contato_detail'),
    path('contatos/<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='contato_update'),
    path('contatos/<int:pk>/excluir/', views.ContatoDeleteView.as_view(), name='contato_delete'),
]
