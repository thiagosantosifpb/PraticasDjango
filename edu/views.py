from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all().order_by('titulo')

    paginator = Paginator(livros, 10)  # 10 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'edu/lista_livros.html', {'page_obj': page_obj})