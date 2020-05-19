from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from clientes.models import Person
from produtos.models import Produto
from django.db.models import Sum, F, FloatField, Max
from .managers import VendaManager

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    impostos = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    nfe_emitida = models.BooleanField(default=False)

    objects = VendaManager()

    class Meta:
        permissions = {
            ('setar_nfe','Usuario pode alterar parametro NFe'),
            ('ver_dashboard', 'Pode visualizar dashboard'),
            ('permissao3', 'Permissao 3'),
        }

    def __str__(self):
        return self.numero + ' - ' + self.pessoa.first_name

    def calcular_total(self):
        tot = self.vendaproduto_set.all().aggregate(
            tot_ped=Sum((F('quantidade') * F('produto__preco')) - F('desconto'), output_field=FloatField())
        )['tot_ped'] or 0

        tot = tot - float(self.impostos) - float(self.desconto)
        Venda.objects.filter(id=self.id).update(valor=tot)

class VendaProduto(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.venda.numero + ' - ' + self.produto.descricao

@receiver(post_save, sender=VendaProduto)
def update_total_vendaproduto(sender,instance,**kwargs):
    instance.venda.calcular_total()

@receiver(post_save, sender=Venda)
def update_total_venda(sender,instance,**kwargs):
    instance.calcular_total()
