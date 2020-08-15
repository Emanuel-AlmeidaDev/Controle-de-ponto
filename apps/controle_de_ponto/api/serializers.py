from rest_framework.serializers import ModelSerializer, SerializerMethodField
from controle_de_ponto.models import Register 

class RegisterSerializer(ModelSerializer):
    tipo = SerializerMethodField()

    class Meta:
        model = Register
        fields = ['id', 'data', 'horario_entrada', 'horario_saida', 'servico']
    
    def get_tipo(self, obj):
        return obj.get_tipo_display()