from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .actions import make_nfe_emitida, make_nfe_nao_emitida

class PersonAdmin(admin.ModelAdmin):
    #fields = (('first_name','last_name'),'age','salary')
    fieldsets = (
        ('Dados Pessoais', {'fields': ('first_name','last_name','age')}),
        ('Dados Complementares', {
            'classes': ('collapse',),
            'fields': ('salary','bio','doc')
        })
    )
    list_filter = ('age','salary')
    list_display = ('first_name','last_name','age','salary','tem_foto')
    search_fields = ('id','first_name',)

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui foto'

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__age','desconto')
    list_display = ('id','pessoa','get_total', 'nfe_emitida')
    search_fields = ('id','pessoa__first_name')
    #raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    readonly_fields = ('valor',)
    actions = [make_nfe_emitida, make_nfe_nao_emitida]
    filter_horizontal = ('produtos',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','preco')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
