from dataclasses import field, fields
from pyexpat import model
from unittest import mock
from .models import Hero
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name','alias')