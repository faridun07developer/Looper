from rest_framework import serializers
from blog.models import Robots


class RobotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robots
        fields = '__all__'
