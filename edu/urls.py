from django.urls import path

from .views import (
    AutorCreateView,
    AutorDeleteView,
    AutorListView,
    AutorUpdateView,
    CadastroUsuarioView,
    EditoraCreateView,
    EditoraDeleteView,
    EditoraListView,
    EditoraUpdateView,
    LivroCreateView,
    LivroDeleteView,
    LivroListView,
    LivroUpdateView,
    PublicaCreateView,
    PublicaDeleteView,
    PublicaListView,
    PublicaUpdateView,
)

urlpatterns = [
    path("livros/", LivroListView.as_view(), name="lista_livros"),
    path("livros/novo/", LivroCreateView.as_view(), name="criar_livro"),
    path("livros/<int:pk>/editar/", LivroUpdateView.as_view(), name="editar_livro"),
    path("livros/<int:pk>/excluir/", LivroDeleteView.as_view(), name="excluir_livro"),
    path("autores/", AutorListView.as_view(), name="lista_autores"),
    path("autores/novo/", AutorCreateView.as_view(), name="criar_autor"),
    path("autores/<int:pk>/editar/", AutorUpdateView.as_view(), name="editar_autor"),
    path("autores/<int:pk>/excluir/", AutorDeleteView.as_view(), name="excluir_autor"),
    path("editoras/", EditoraListView.as_view(), name="lista_editoras"),
    path("editoras/novo/", EditoraCreateView.as_view(), name="criar_editora"),
    path("editoras/<int:pk>/editar/", EditoraUpdateView.as_view(), name="editar_editora"),
    path("editoras/<int:pk>/excluir/", EditoraDeleteView.as_view(), name="excluir_editora"),
    path("publicacoes/", PublicaListView.as_view(), name="lista_publicacoes"),
    path("publicacoes/novo/", PublicaCreateView.as_view(), name="criar_publicacao"),
    path(
        "publicacoes/<int:pk>/editar/",
        PublicaUpdateView.as_view(),
        name="editar_publicacao",
    ),
    path(
        "publicacoes/<int:pk>/excluir/",
        PublicaDeleteView.as_view(),
        name="excluir_publicacao",
    ),
    path("accounts/signup/", CadastroUsuarioView.as_view(), name="signup"),
]
