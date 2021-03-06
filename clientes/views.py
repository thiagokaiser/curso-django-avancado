from django.forms import model_to_dict
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from .forms import PersonForm
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from clientes.models import Person
from produtos.models import Produto
from vendas.models import Venda
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View

############# FBV #############
@login_required
def persons_list(request):
    search = request.GET.get('search', '')
    if search == '':
        persons = Person.objects.all()
    else:
        persons = Person.objects.filter(first_name__icontains=search) |  Person.objects.filter(last_name__icontains=search)

    return render(request, 'person.html', {'persons': persons, 'search': search})

@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('nao autorizado')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('clientes:person_list')
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('clientes:person_list')

    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('clientes:person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

def tags_filters(request):
    teste_filter = 'Ola mundo'
    return render(request,'tags_filters.html', {'teste_filter': teste_filter})

def api(request):
    prod = Produto.objects.last()
    result = model_to_dict(prod)
    return JsonResponse(result, status=200)

############# CBV #############
class PersonList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'clientesCBV/person_list.html'
    permission_required = ('clientes.list_person')
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        return Person.objects.filter(first_name__icontains=search) |  Person.objects.filter(last_name__icontains=search)


class PersonDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'clientesCBV/person_detail.html'
    permission_required = ('clientes.list_person')
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(pessoa_id=self.object.id)
        return context

class PersonCreate(LoginRequiredMixin, CreateView):
    template_name = 'clientesCBV/person_form.html'
    model = Person
    fields = ['first_name','last_name','age','salary','bio','photo']
    #success_url = reverse_lazy('person_list_cbv')
    def get_success_url(self):
        return reverse_lazy('clientes:person_list_cbv')

class PersonUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'clientesCBV/person_update_form.html'
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url =  reverse_lazy('clientes:person_list_cbv')

class PersonDelete(LoginRequiredMixin, DeleteView):
    template_name = 'clientesCBV/person_confirm_delete.html'
    model = Person
    success_url =  reverse_lazy('clientes:person_list_cbv')

class TesteTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'testeCBV.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'TemplateView'

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)
        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context

class TesteView(LoginRequiredMixin, View):
    def get(self, request):
        response = render_to_response('testeCBV.html')

        response.set_cookie('color','blue', max_age=1000)
        mycookie = request.COOKIES.get('color')
        print(mycookie)

        return response

    def post(self, request):
        return HttpResponse('result post')

class ProdutoBulk(LoginRequiredMixin, View):
    def get(self, request):
        produtos = ['banana', 'maca', 'limao', 'laranja', 'pera', 'melancia']
        list_produtos = []
        for produto in produtos:
            p = Produto(descricao=produto,preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('funcionou')