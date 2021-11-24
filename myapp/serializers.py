from rest_framework.serializers import ModelSerializer

from .models import AliBahi


class AliBahiSeriliaer(ModelSerializer):
    class Meta:
        model = AliBahi
        fields = '__all__'
