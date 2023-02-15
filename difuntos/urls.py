from django.urls import path
from . import views

template_base = "difuntos"

urlpatterns = [
    path("", views.index, name=f'{template_base}_index'),
    path("create", views.create, name=f'{template_base}_create'),
    path("update/<int:id>", views.create, name=f'{template_base}_update'),
    path("show/<int:id>", views.create, name=f'{template_base}_show'),
    path("delete/<int:id>", views.create, name=f'{template_base}_delete'),
]
