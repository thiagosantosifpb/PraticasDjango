from decimal import Decimal
import random

from django.core.management.base import BaseCommand
from faker import Faker

from edu.models import Autor, Editora, Livro, Publica


class Command(BaseCommand):
    help = "Gera livros com dados fake para testar a paginação e os CRUDs."

    def add_arguments(self, parser):
        parser.add_argument(
            "--quantidade",
            type=int,
            default=100,
            help="Quantidade de livros a serem gerados. Padrão: 100.",
        )

    def handle(self, *args, **kwargs):
        quantidade = kwargs["quantidade"]
        fake = Faker("pt_BR")

        editora, _ = Editora.objects.get_or_create(nome="Editora Faker")
        autor, _ = Autor.objects.get_or_create(nome="Autor Faker")

        criados = 0
        tentativas = 0
        limite_tentativas = quantidade * 5

        while criados < quantidade and tentativas < limite_tentativas:
            tentativas += 1
            isbn = fake.isbn13(separator="")[:13]

            if Livro.objects.filter(isbn=isbn).exists():
                continue

            livro = Livro.objects.create(
                isbn=isbn,
                titulo=fake.sentence(nb_words=4).rstrip("."),
                publicacao=fake.date_between(start_date="-20y", end_date="today"),
                preco=Decimal(str(round(random.uniform(20, 150), 2))),
                estoque=random.randint(0, 100),
                editora=editora,
            )
            Publica.objects.get_or_create(livro=livro, autor=autor)
            criados += 1

        self.stdout.write(
            self.style.SUCCESS(f"{criados} livro(s) criado(s) com sucesso!")
        )
