from django.contrib import admin
from .models import Person, Documento

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

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
