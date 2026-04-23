from django.contrib import admin
from .models import Autor, Editora, Livro, Publica


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    list_per_page = 10


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'isbn', 'editora', 'preco', 'estoque')
    search_fields = ('titulo', 'isbn')
    list_filter = ('editora',)
    ordering = ('titulo',)
    list_per_page = 10


@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'livro', 'autor')
    list_filter = ('autor', 'livro')
    list_per_page = 10