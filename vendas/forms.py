from django import forms
from .models import Produto

class VendaProdutoForm(forms.Form):
    produto_id = forms.ModelChoiceField(queryset=Produto.objects.all())
    quantidade = forms.IntegerField(label="Quantidade")
    desconto = forms.DecimalField(label="Desconto", max_digits=7, decimal_places=2)