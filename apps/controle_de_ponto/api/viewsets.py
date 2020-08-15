from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer
from ..models import Register 

class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer