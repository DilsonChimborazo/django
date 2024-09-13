from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.viewsets import modelViewSet

# Create your views here.
class TareaViewSet(modelViewSet):
    queryset = Tarea.objects.all()
    serializers_class = TareaSerializer