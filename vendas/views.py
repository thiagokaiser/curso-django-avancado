from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Venda

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
