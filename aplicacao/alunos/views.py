from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    alunos = {
        1: 'Aluno 1',
        2: 'Aluno 2',
        3: 'Aluno 3',
        4: 'Aluno 4',
        5: 'Aluno 5',
        6: 'Aluno 6',
    }
    dados = {
        'nome_do_aluno' : alunos
    }

    return render(request,'index.html', dados)

def aluno(request):
    return render(request,'aluno.html')