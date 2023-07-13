from rest_framework.viewsets import ModelViewSet
from .models import Empanada
from .serializer import EmpanadaSerializer


class EmpanadaViewSet(ModelViewSet):
    queryset = Empanada.objects.all()   ## "todo" lo que vamos a integrar-- trea todos los datos de la tabla de empanada
    serializer_class = EmpanadaSerializer