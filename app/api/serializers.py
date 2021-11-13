import api.models as models
from rest_framework import serializers

class ResortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Resort
        fields = ['id', 'name', 'description', 'country']

class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Country
        fields =  ['id', 'name', 'code', 'iso_code']

class TourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tour
        fields = ['id', 'resort', 'description', 'takeoff_time', 'end_time']