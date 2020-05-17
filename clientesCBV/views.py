from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse_lazy
from clientesFBV.models import Person
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View

class PersonList(ListView):
    template_name = 'clientes/person_list.html'
    model = Person

class PersonDetail(DetailView):
    template_name = 'clientes/person_detail.html'
    model = Person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreate(CreateView):
    template_name = 'clientes/person_form.html'
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo']
    #success_url = reverse_lazy('person_list_cbv')
    def get_success_url(self):
        return reverse_lazy('clientesCBV:person_list_cbv')

class PersonUpdate(UpdateView):
    template_name = 'clientes/person_update_form.html'
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url =  reverse_lazy('clientesCBV:person_list_cbv')

class PersonDelete(DeleteView):
    template_name = 'clientes/person_confirm_delete.html'
    model = Person
    success_url =  reverse_lazy('clientesCBV:person_list_cbv')

class TesteTemplateView(TemplateView):
    template_name = 'testeCBV.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'testando templateview'
        return context

class TesteView(View):
    def get(self, request):
        return render(request, 'testeCBV.html')

    def post(self, request):
        return HttpResponse('result post')
