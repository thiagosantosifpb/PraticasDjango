from rest_framework.viewsets import ModelViewSet

from .models import Autor, Editora
from .serializers import AutorSerializer, EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all().order_by('nome')
    serializer_class = AutorSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all().order_by('nome')
    serializer_class = EditoraSerializer