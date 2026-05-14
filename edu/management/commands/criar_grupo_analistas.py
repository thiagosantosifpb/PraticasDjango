from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from edu.models import Livro


class Command(BaseCommand):
    help = "Cria o grupo de analistas de cadastro de produtos com permissões para gerenciar livros."

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(
            name="Analistas de cadastro de produtos"
        )
        content_type = ContentType.objects.get_for_model(Livro)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=["view_livro", "add_livro", "change_livro", "delete_livro"],
        )
        group.permissions.set(permissions)

        status = "criado" if created else "atualizado"
        self.stdout.write(
            self.style.SUCCESS(
                f"Grupo '{group.name}' {status} com permissões de visualização, cadastro, edição e remoção de livros."
            )
        )
