from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastrar_candidato, name='cadastro'),
]