from django.urls import path
from .views import DashboardView, NovoProdVenda, ListaVendas, EditVenda, DelVenda, DelProdVenda

app_name = 'vendas'

urlpatterns = [
    path('', ListaVendas.as_view(), name="venda_list"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('edit_venda/<int:id>/', EditVenda.as_view(), name="edit_venda"),
    path('novo_prod_venda/<int:id>/', NovoProdVenda.as_view(), name="novo_prod_venda"),
    path('del_venda/<int:id>/', DelVenda.as_view(), name="del_venda"),
    path('del_prod_venda/<int:id>/', DelProdVenda.as_view(), name="del_prod_venda"),
]