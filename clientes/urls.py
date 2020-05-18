from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import tags_filters
from .views import PersonList, PersonDetail
from .views import PersonCreate, PersonUpdate, PersonDelete
from .views import TesteView, TesteTemplateView, ProdutoBulk

app_name = 'clientes'

urlpatterns = [
    path('', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),
    path('tags_filters/', tags_filters, name="tags_filters"),
    path('cbv/', PersonList.as_view(), name="person_list_cbv"),
    path('cbv/detail/<int:pk>/', PersonDetail.as_view(), name="person_detail_cbv"),
    path('cbv/new/', PersonCreate.as_view(), name="person_new_cbv"),
    path('cbv/update/<int:pk>/', PersonUpdate.as_view(), name="person_update_cbv"),
    path('cbv/delete/<int:pk>/', PersonDelete.as_view(), name="person_delete_cbv"),
    path('cbv/templateview/', TesteTemplateView.as_view()),
    path('cbv/view/', TesteView.as_view()),
    path('cbv/produto_bulk/', ProdutoBulk.as_view(), name='produto_bulk'),
]