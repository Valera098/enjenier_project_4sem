from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
import api.serializers as serializers
import api.models as models

class ResortViewSet(viewsets.ModelViewSet):
    queryset = models.Resort.objects.all()
    serializer_class = serializers.ResortSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, permissions.IsAuthenticated]

class TourViewSet(viewsets.ModelViewSet):
    queryset = models.Tour.objects.all()
    serializer_class = serializers.TourSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
