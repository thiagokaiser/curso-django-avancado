from django.contrib import admin
from .models import Venda, VendaProduto
from .actions import make_nfe_emitida, make_nfe_nao_emitida

class VendaProdutoInline(admin.TabularInline):
    model = VendaProduto
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__age','desconto')
    list_display = ('id','pessoa', 'nfe_emitida')
    search_fields = ('id','pessoa__first_name')
    #raw_id_fields = ('pessoa',)
    # filter_horizontal = ('produtos',)
    autocomplete_fields = ('pessoa',)
    readonly_fields = ('valor',)
    actions = [make_nfe_emitida, make_nfe_nao_emitida]
    inlines = [VendaProdutoInline]

admin.site.register(Venda, VendaAdmin)
admin.site.register(VendaProduto)