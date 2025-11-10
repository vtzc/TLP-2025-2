from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.Serializer):
     class Meta:
        model = Producto
        fields = ["codigo", "descripcion", "precio"]
        