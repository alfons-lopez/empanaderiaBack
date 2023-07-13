from rest_framework.serializers import ModelSerializer
from .models import Empanada

class EmpanadaSerializer(ModelSerializer):
    class Meta:
        model = Empanada
        fields = "__all__"   ## serialize todos los campos -- se puede especificar





# el serializador tiene que conectarse con viewsets
# el viewsets va a permitir generar los distintos canales de creacion, borrado, actualizacion para una api 