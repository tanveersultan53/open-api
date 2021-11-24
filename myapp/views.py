from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import AliBahiSeriliaer
from .models import AliBahi


# Create your views here.


class AliBahiView(GenericAPIView):
    serializer_class = AliBahiSeriliaer
    queryset = AliBahi.objects.all()

    def get(self, request, *args, **kwargs):
        obj = AliBahi.objects.all()
        serializer = self.get_serializer(obj,many=True)
        return Response(data= serializer.data)

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)