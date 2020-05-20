from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib import messages
from .models import Venda, VendaProduto
from clientes.models import Person
from .forms import VendaProdutoForm

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desc()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['count'] = Venda.objects.count()
        data['count_nfe'] = Venda.objects.count_nfe()

        return render(request, 'vendas/dashboard.html', data)

class EditVenda(View):
    def get(self, request, id):
        data = {}
        data['form_prod'] = VendaProdutoForm()
        data['venda_id'] = id
        if id != 0:
            venda = Venda.objects.get(id=id)
            data['numero'] = venda.numero
            data['desconto'] = float(venda.desconto)
            data['venda'] = venda
            data['produtos'] = venda.vendaproduto_set.all()
        else:
            data['clientes'] = Person.objects.all()

        return render(request, 'vendas/venda_form.html', data)

    def post(self, request, id):
        numero = request.POST.get('numero','')
        cliente = request.POST.get('cliente', '')
        venda_id = request.POST.get('venda_id', '')
        desconto = request.POST.get('desconto', '')
        if desconto == '':
            desconto = 0
        else:
            desconto = float(desconto)

        if venda_id != '0':
            venda = Venda.objects.get(id=venda_id)
            venda.desconto = desconto
            venda.save()
        else:
            cliente = Person.objects.get(id=cliente)
            venda = Venda.objects.create(
                numero=numero, desconto=desconto, pessoa=cliente)

        return redirect('vendas:edit_venda', id=venda.id)

class NovoProdVenda(View):
    def post(self, request, id):
        prod = VendaProduto.objects.filter(produto_id=request.POST['produto_id'], venda_id=id)
        if prod.exists():
            messages.error(request, 'Item já incluido na venda')
            return redirect('vendas:edit_venda', id=prod[0].venda.id)
        else:
            produto = request.POST.get('produto_id')
            quantidade = request.POST.get('quantidade')
            desconto = request.POST.get('desconto')
            prod = VendaProduto.objects.create(
                produto_id=produto, quantidade=quantidade,
                desconto=desconto, venda_id=id)
            return redirect('vendas:edit_venda', id=prod.venda.id)

class ListaVendas(View):
    def get(self, request):
        data = {}
        data['vendas'] = Venda.objects.all()
        return render(request,'vendas/venda_list.html', data)

class DelVenda(View):
    def get(self, request, id):
        venda = Venda.objects.get(id=id)
        return render(request, 'vendas/del_venda_confirm.html', {'venda': venda})

    def post(self, request, id):
        venda = Venda.objects.get(id=id)
        venda.delete()
        return redirect('vendas:venda_list')

class DelProdVenda(View):
    def get(self, request, id):
        prod = VendaProduto.objects.get(id=id)
        return render(request, 'vendas/del_prod_venda_confirm.html', {'prod': prod})

    def post(self, request, id):
        prod = VendaProduto.objects.get(id=id)
        venda_id = prod.venda.id
        prod.delete()
        return redirect('vendas:edit_venda', id=venda_id)

