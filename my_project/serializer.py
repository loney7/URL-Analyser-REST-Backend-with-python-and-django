from rest_framework import serializers
from .models import Webpage

class Webpageserializer(serializers.ModelSerializer):
    class Meta:
        model = Webpage
