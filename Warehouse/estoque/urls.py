from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos),
    path('<int:produto_id>/', views.detalhes_produto),
]
