from rest_framework.serializers import modelserializer
from .models import Tarea

class TareaSerializer(modelserializer):
    class Meta:
        model = Tarea
        fields='__all__'