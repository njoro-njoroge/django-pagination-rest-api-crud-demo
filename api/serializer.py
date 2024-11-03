from rest_framework import serializers
from .models import Fruit


class FruitSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fruit
        fields = ['url','id', 'fruit_name', 'stock']
