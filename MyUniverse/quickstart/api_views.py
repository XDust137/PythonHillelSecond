from rest_framework import viewsets

from quickstart.serializer import GalaxySerializer, PlanetSerializer, StarSerializer, StarSystemSerializer, MoonSerializer
from quickstart.models import Galaxy, Planet, Star, StarSystem, Moon


class GalaxyViewSet(viewsets.ModelViewSet):
    queryset = Galaxy.objects.all()
    serializer_class = GalaxySerializer


class StarSystemViewSet(viewsets.ModelViewSet):
    queryset = StarSystem.objects.all()
    serializer_class = StarSystemSerializer


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class MoonViewSet(viewsets.ModelViewSet):
    queryset = Moon.objects.all()
    serializer_class = PlanetSerializer
