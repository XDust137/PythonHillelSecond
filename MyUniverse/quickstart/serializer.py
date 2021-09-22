import re

from rest_framework import serializers

from quickstart.models import Galaxy, Planet, Star, StarSystem, Moon


class GalaxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Galaxy

        fields = [
            'pk',
            "name",
            "size_x",
            "size_y",
            "shape",
        ]


class StarSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarSystem

        fields = [
            'pk',
            "name",
            "pos_x",
            "pos_y",
            "galaxy",
        ]


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star

        fields = [
            'pk',
            "name",
            "star_system",
            "type",
            "diameter",
            "S",
            "age_in_centuries",
            "mass_in_suns",
        ]


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet

        fields = [
            'pk',
            'name',
            'star_system',
            'color',
            "atmosphere",
            "habitable",
            "diameter",
            "S",
            "age_in_centuries",
            "mass_in_suns",
        ]


class MoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moon

        fields = [
            'pk',
            'name',
            'planet',
            'color',
            "atmosphere",
            "habitable",
            "diameter",
            "S",
            "age_in_centuries",
            "mass_in_suns",
        ]
