from django.test import TestCase
from django.urls import reverse

from .models import Contato


class ContatoListViewTests(TestCase):
    """Testes para a rota de listagem: '' -> contato_list"""

    def setUp(self):
        self.amigo = Contato.objects.create(
            nome='Ana Amiga', telefone='11911111111', categoria=Contato.Categoria.AMIGOS
        )
        self.familiar = Contato.objects.create(
            nome='Beto Familia', telefone='11922222222', categoria=Contato.Categoria.FAMILIA
        )

    def test_status_code_e_template(self):
        response = self.client.get(reverse('contato_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/contato_list.html')

    def test_lista_todos_os_contatos(self):
        response = self.client.get(reverse('contato_list'))
        self.assertContains(response, 'Ana Amiga')
        self.assertContains(response, 'Beto Familia')

    def test_filtra_por_categoria_amigos(self):
        response = self.client.get(reverse('contato_list'), {'categoria': 'amigos'})
        self.assertContains(response, 'Ana Amiga')
        self.assertNotContains(response, 'Beto Familia')

    def test_filtra_por_categoria_familia(self):
        response = self.client.get(reverse('contato_list'), {'categoria': 'familia'})
        self.assertContains(response, 'Beto Familia')
        self.assertNotContains(response, 'Ana Amiga')

    def test_lista_vazia(self):
        Contato.objects.all().delete()
        response = self.client.get(reverse('contato_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhum contato cadastrado')


class ContatoDetailViewTests(TestCase):
    """Testes para a rota de detalhe: 'contatos/<id>/' -> contato_detail"""

    def setUp(self):
        self.contato = Contato.objects.create(
            nome='Carlos Silva', telefone='11933333333', categoria=Contato.Categoria.AMIGOS
        )

    def test_status_code_e_template(self):
        response = self.client.get(reverse('contato_detail', args=[self.contato.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/contato_detail.html')

    def test_exibe_dados_do_contato(self):
        response = self.client.get(reverse('contato_detail', args=[self.contato.pk]))
        self.assertContains(response, 'Carlos Silva')
        self.assertContains(response, '11933333333')
        self.assertContains(response, 'Amigos')

    def test_contato_inexistente_retorna_404(self):
        response = self.client.get(reverse('contato_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)


class ContatoCreateViewTests(TestCase):
    """Testes para a rota de criação: 'contatos/novo/' -> contato_create"""

    def test_get_status_code_e_template(self):
        response = self.client.get(reverse('contato_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/contato_form.html')

    def test_post_dados_validos_cria_contato_e_redireciona(self):
        dados = {'nome': 'Diana Nova', 'telefone': '11944444444', 'categoria': 'familia'}
        response = self.client.post(reverse('contato_create'), dados)
        self.assertRedirects(response, reverse('contato_list'))
        self.assertEqual(Contato.objects.count(), 1)
        contato = Contato.objects.first()
        self.assertEqual(contato.nome, 'Diana Nova')
        self.assertEqual(contato.categoria, 'familia')

    def test_post_dados_invalidos_nao_cria_contato(self):
        dados = {'nome': '', 'telefone': '', 'categoria': ''}
        response = self.client.post(reverse('contato_create'), dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contato.objects.count(), 0)
        self.assertFormError(response.context['form'], 'nome', 'Este campo é obrigatório.')

    def test_post_categoria_invalida_nao_cria_contato(self):
        dados = {'nome': 'Eva', 'telefone': '11955555555', 'categoria': 'trabalho'}
        response = self.client.post(reverse('contato_create'), dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contato.objects.count(), 0)


class ContatoUpdateViewTests(TestCase):
    """Testes para a rota de edição: 'contatos/<id>/editar/' -> contato_update"""

    def setUp(self):
        self.contato = Contato.objects.create(
            nome='Fabio Antigo', telefone='11966666666', categoria=Contato.Categoria.AMIGOS
        )

    def test_get_status_code_e_template(self):
        response = self.client.get(reverse('contato_update', args=[self.contato.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/contato_form.html')

    def test_get_formulario_preenchido_com_dados_atuais(self):
        response = self.client.get(reverse('contato_update', args=[self.contato.pk]))
        self.assertContains(response, 'Fabio Antigo')

    def test_post_dados_validos_atualiza_contato_e_redireciona(self):
        dados = {'nome': 'Fabio Editado', 'telefone': '11977777777', 'categoria': 'familia'}
        response = self.client.post(reverse('contato_update', args=[self.contato.pk]), dados)
        self.assertRedirects(response, reverse('contato_list'))
        self.contato.refresh_from_db()
        self.assertEqual(self.contato.nome, 'Fabio Editado')
        self.assertEqual(self.contato.telefone, '11977777777')
        self.assertEqual(self.contato.categoria, 'familia')

    def test_post_dados_invalidos_nao_atualiza_contato(self):
        dados = {'nome': '', 'telefone': '11977777777', 'categoria': 'familia'}
        response = self.client.post(reverse('contato_update', args=[self.contato.pk]), dados)
        self.assertEqual(response.status_code, 200)
        self.contato.refresh_from_db()
        self.assertEqual(self.contato.nome, 'Fabio Antigo')

    def test_contato_inexistente_retorna_404(self):
        response = self.client.get(reverse('contato_update', args=[9999]))
        self.assertEqual(response.status_code, 404)


class ContatoDeleteViewTests(TestCase):
    """Testes para a rota de exclusão: 'contatos/<id>/excluir/' -> contato_delete"""

    def setUp(self):
        self.contato = Contato.objects.create(
            nome='Gustavo Remover', telefone='11988888888', categoria=Contato.Categoria.FAMILIA
        )

    def test_get_status_code_e_template_confirmacao(self):
        response = self.client.get(reverse('contato_delete', args=[self.contato.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/contato_confirm_delete.html')
        self.assertContains(response, 'Gustavo Remover')

    def test_post_remove_contato_e_redireciona(self):
        response = self.client.post(reverse('contato_delete', args=[self.contato.pk]))
        self.assertRedirects(response, reverse('contato_list'))
        self.assertFalse(Contato.objects.filter(pk=self.contato.pk).exists())

    def test_contato_inexistente_retorna_404(self):
        response = self.client.get(reverse('contato_delete', args=[9999]))
        self.assertEqual(response.status_code, 404)
