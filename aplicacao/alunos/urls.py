from django.urls import path
from . import views #importacao da pasta raiz 'alunos'

urlpatterns = [
    path ('', views.index, name='index'),
    path ('aluno/', views.aluno, name='aluno'),
]