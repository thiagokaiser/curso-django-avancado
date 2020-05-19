from django.http import HttpResponseForbidden

def make_nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseForbidden('<h1>Sem permissao</h1>')

def make_nfe_nao_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=False)
    else:
        return HttpResponseForbidden('<h1>Sem permissao</h1>')

make_nfe_emitida.short_description = "Nota Emitida"
make_nfe_nao_emitida.short_description = "Nota não Emitida"