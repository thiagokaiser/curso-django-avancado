from django.shortcuts import render
from django.views import View
from .models import Venda

class DashboardView(View):
    def get(self, request):
        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desc()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['count'] = Venda.objects.count()
        data['count_nfe'] = Venda.objects.count_nfe()

        return render(request, 'vendas/dashboard.html', data)
