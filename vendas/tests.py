from django.test import TestCase
from vendas.models import Venda, VendaProduto
from produtos.models import Produto

class VendaTestCase(TestCase):
    def setUp(self):
        self.venda = Venda.objects.create(numero=123, desconto=0, impostos=0)
        self.produto = Produto.objects.create(descricao='teste 01', preco=10)

    def test_verifica_num_vendas(self):
        assert Venda.objects.all().count() == 1

    def test_valor_venda(self):
        # Verifica valor total da venda
        VendaProduto.objects.create(
            venda=self.venda, produto=self.produto, quantidade=1, desconto=1)
        test = Venda.objects.get(numero=123)

        self.assertEqual(test.valor, 9)

    def test_desconto(self):
        self.assertNotEqual(self.venda.desconto, 1)

    def test_prod_incluido_venda(self):
        prod = VendaProduto.objects.create(
            venda=self.venda, produto=self.produto, quantidade=2, desconto=3)

        self.assertIn(prod, self.venda.vendaproduto_set.all())

    def test_nfe_emitida(self):
        self.assertFalse(self.venda.nfe_emitida)