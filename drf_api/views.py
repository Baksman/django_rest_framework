from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemsSerilizer
from .models import Items


class TestView(APIView):

    def get(self,request,*args,**kwargs):
        qs = Items.objects.all().first()
        serializer = ItemsSerilizer(qs)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = ItemsSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Create your views here.
