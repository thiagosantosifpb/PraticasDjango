from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import date

from edu.models import Livro, Editora, Autor, Publica


class Command(BaseCommand):
    help = 'Gera 100 livros com dados fake'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_BR')

        # cria editora padrão
        editora, _ = Editora.objects.get_or_create(nome="Editora Faker")

        # cria autor padrão
        autor, _ = Autor.objects.get_or_create(nome="Autor Faker")

        for _ in range(100):
            livro = Livro.objects.create(
                isbn=fake.isbn13(),
                titulo=fake.sentence(nb_words=4),
                publicacao=fake.date_between(start_date='-20y', end_date='today'),
                preco=round(random.uniform(20, 150), 2),
                estoque=random.randint(0, 100),
                editora=editora
            )

            Publica.objects.create(
                livro=livro,
                autor=autor
            )

        self.stdout.write(self.style.SUCCESS('100 livros criados com sucesso!'))