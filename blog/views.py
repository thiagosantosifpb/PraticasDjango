from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone


def welcome(request):
    return HttpResponse('Bem-vindo ao meu blog!')


def eco(request, texto):
    return HttpResponse(f'Você digitou: {texto}')


def info(request):
    data = {
        'disciplina': 'RAD',
        'framework': 'Django',
        'semestre': '2025.2',
    }
    return JsonResponse(data)


def home(request):
    contexto = {
        'usuario': 'Thiago Alexandre',
        'now': timezone.now(),
        'is_logged_in': True,
        'role': 'admin',
        'produtos': [
            {'nome': 'Notebook', 'preco': 3500.00},
            {'nome': 'Mouse', 'preco': 89.90},
            {'nome': 'Teclado', 'preco': 149.90},
        ],
        'telefone_contato': '83999990000',
    }
    return render(request, 'blog/home.html', contexto)


def contato(request, telefone):
    contexto = {
        'telefone': telefone,
        'now': timezone.now(),
    }
    return render(request, 'blog/contato.html', contexto)
