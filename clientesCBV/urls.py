from django.urls import path
from .views import PersonList, PersonDetail
from .views import PersonCreate, PersonUpdate, PersonDelete
from .views import TesteView, TesteTemplateView

app_name = 'clientesCBV'

urlpatterns = [
    path('', PersonList.as_view(), name="person_list_cbv"),
    path('detail/<int:pk>/', PersonDetail.as_view(), name="person_detail_cbv"),
    path('new/', PersonCreate.as_view(), name="person_new_cbv"),
    path('update/<int:pk>/', PersonUpdate.as_view(), name="person_update_cbv"),
    path('delete/<int:pk>/', PersonDelete.as_view(), name="person_delete_cbv"),
    path('templateview/', TesteTemplateView.as_view()),
    path('view/', TesteView.as_view()),
]