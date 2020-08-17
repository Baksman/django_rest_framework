from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ItemsSerilizer
from .models import Items


class ItemsView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = ItemsSerilizer
    queryset = Items.objects.all()
    def get(self, request, *args, **kwargs):
        return self.list(self,request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



class ItemsCreateView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class = ItemsSerilizer
    queryset = Items.objects.all()
         
    def get(self, request, *args, **kwargs):
        return self.list(self,request,*args,**kwargs)



# class TestView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Items.objects.all().first()
#         serializer = ItemsSerilizer(qs)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = ItemsSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# Create your views here.
