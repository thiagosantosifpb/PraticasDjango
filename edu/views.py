from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import AutorForm, CadastroUsuarioForm, EditoraForm, LivroForm, PublicaForm
from .models import Autor, Editora, Livro, Publica


class CadastroUsuarioView(CreateView):
    form_class = CadastroUsuarioForm
    template_name = "edu/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Usuário cadastrado com sucesso. Faça login para acessar as rotas protegidas.",
        )
        return response


class ListaGenericaView(ListView):
    template_name = "edu/lista_generica.html"
    paginate_by = 10
    columns = []
    titulo = "Registros"
    create_url_name = None
    edit_url_name = None
    delete_url_name = None
    create_permission = None
    change_permission = None
    delete_permission = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        def pode(permission=None):
            if not user.is_authenticated:
                return False
            return user.has_perm(permission) if permission else True

        context.update(
            {
                "titulo": self.titulo,
                "columns": self.columns,
                "rows": [
                    {
                        "object": obj,
                        "values": [getattr(obj, attr) for _, attr in self.columns],
                    }
                    for obj in context["object_list"]
                ],
                "create_url_name": self.create_url_name,
                "edit_url_name": self.edit_url_name,
                "delete_url_name": self.delete_url_name,
                "pode_criar": pode(self.create_permission),
                "pode_editar": pode(self.change_permission),
                "pode_excluir": pode(self.delete_permission),
            }
        )
        return context


class LoginObrigatorioMixin(LoginRequiredMixin):
    login_url = reverse_lazy("login")


class AutorListView(ListaGenericaView):
    model = Autor
    ordering = ["nome"]
    titulo = "Autores"
    columns = [("Nome", "nome")]
    create_url_name = "criar_autor"
    edit_url_name = "editar_autor"
    delete_url_name = "excluir_autor"


class AutorCreateView(LoginObrigatorioMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_autores")
    extra_context = {"titulo": "Cadastrar autor", "url_cancelar": "lista_autores"}


class AutorUpdateView(LoginObrigatorioMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_autores")
    extra_context = {"titulo": "Editar autor", "url_cancelar": "lista_autores"}


class AutorDeleteView(LoginObrigatorioMixin, DeleteView):
    model = Autor
    template_name = "edu/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_autores")
    extra_context = {"titulo": "Excluir autor", "url_cancelar": "lista_autores"}


class EditoraListView(ListaGenericaView):
    model = Editora
    ordering = ["nome"]
    titulo = "Editoras"
    columns = [("Nome", "nome")]
    create_url_name = "criar_editora"
    edit_url_name = "editar_editora"
    delete_url_name = "excluir_editora"


class EditoraCreateView(LoginObrigatorioMixin, CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_editoras")
    extra_context = {"titulo": "Cadastrar editora", "url_cancelar": "lista_editoras"}


class EditoraUpdateView(LoginObrigatorioMixin, UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_editoras")
    extra_context = {"titulo": "Editar editora", "url_cancelar": "lista_editoras"}


class EditoraDeleteView(LoginObrigatorioMixin, DeleteView):
    model = Editora
    template_name = "edu/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_editoras")
    extra_context = {"titulo": "Excluir editora", "url_cancelar": "lista_editoras"}


class LivroListView(ListaGenericaView):
    model = Livro
    ordering = ["titulo"]
    titulo = "Livros"
    columns = [
        ("Título", "titulo"),
        ("ISBN", "isbn"),
        ("Editora", "editora"),
        ("Publicação", "publicacao"),
        ("Preço", "preco"),
        ("Estoque", "estoque"),
    ]
    create_url_name = "criar_livro"
    edit_url_name = "editar_livro"
    delete_url_name = "excluir_livro"
    create_permission = "edu.add_livro"
    change_permission = "edu.change_livro"
    delete_permission = "edu.delete_livro"

    def get_queryset(self):
        return Livro.objects.select_related("editora").order_by("titulo")


class LivroCreateView(LoginObrigatorioMixin, PermissionRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_livros")
    permission_required = "edu.add_livro"
    permission_denied_message = "Você não possui permissão para cadastrar livros."
    extra_context = {"titulo": "Cadastrar livro", "url_cancelar": "lista_livros"}


class LivroUpdateView(LoginObrigatorioMixin, PermissionRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_livros")
    permission_required = "edu.change_livro"
    permission_denied_message = "Você não possui permissão para editar livros."
    extra_context = {"titulo": "Editar livro", "url_cancelar": "lista_livros"}


class LivroDeleteView(LoginObrigatorioMixin, PermissionRequiredMixin, DeleteView):
    model = Livro
    template_name = "edu/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_livros")
    permission_required = "edu.delete_livro"
    permission_denied_message = "Você não possui permissão para remover livros."
    extra_context = {"titulo": "Excluir livro", "url_cancelar": "lista_livros"}


class PublicaListView(ListaGenericaView):
    model = Publica
    ordering = ["livro__titulo", "autor__nome"]
    titulo = "Publicações"
    columns = [("Livro", "livro"), ("Autor", "autor")]
    create_url_name = "criar_publicacao"
    edit_url_name = "editar_publicacao"
    delete_url_name = "excluir_publicacao"

    def get_queryset(self):
        return Publica.objects.select_related("livro", "autor").order_by(
            "livro__titulo", "autor__nome"
        )


class PublicaCreateView(LoginObrigatorioMixin, CreateView):
    model = Publica
    form_class = PublicaForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_publicacoes")
    extra_context = {"titulo": "Cadastrar publicação", "url_cancelar": "lista_publicacoes"}


class PublicaUpdateView(LoginObrigatorioMixin, UpdateView):
    model = Publica
    form_class = PublicaForm
    template_name = "edu/form_generico.html"
    success_url = reverse_lazy("lista_publicacoes")
    extra_context = {"titulo": "Editar publicação", "url_cancelar": "lista_publicacoes"}


class PublicaDeleteView(LoginObrigatorioMixin, DeleteView):
    model = Publica
    template_name = "edu/confirmar_exclusao.html"
    success_url = reverse_lazy("lista_publicacoes")
    extra_context = {"titulo": "Excluir publicação", "url_cancelar": "lista_publicacoes"}
