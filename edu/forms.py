from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Autor, Editora, Livro, Publica


class BootstrapFormMixin:
    """Aplica classes CSS simples aos campos dos formulários."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = "form-control"
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(field.widget, forms.Select):
                css_class = "form-select"
            current_class = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{current_class} {css_class}".strip()


class AutorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nome"]
        labels = {"nome": "Nome do autor"}


class EditoraForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Editora
        fields = ["nome"]
        labels = {"nome": "Nome da editora"}


class LivroForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["isbn", "titulo", "publicacao", "preco", "estoque", "editora"]
        labels = {
            "isbn": "ISBN",
            "titulo": "Título",
            "publicacao": "Data de publicação",
            "preco": "Preço",
            "estoque": "Estoque",
            "editora": "Editora",
        }
        widgets = {
            "publicacao": forms.DateInput(attrs={"type": "date"}),
            "preco": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "estoque": forms.NumberInput(attrs={"min": "0"}),
        }


class PublicaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Publica
        fields = ["livro", "autor"]
        labels = {"livro": "Livro", "autor": "Autor"}


class CadastroUsuarioForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(required=False, label="E-mail")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Usuário",
            "password1": "Senha",
            "password2": "Confirmação de senha",
        }
