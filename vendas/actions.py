def make_nfe_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=True)

def make_nfe_nao_emitida(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

make_nfe_emitida.short_description = "Nota Emitida"
make_nfe_nao_emitida.short_description = "Nota não Emitida"