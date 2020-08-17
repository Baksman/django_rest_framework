from rest_framework import serializers
from .models import Items



class ItemsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ("title","description","owner")
