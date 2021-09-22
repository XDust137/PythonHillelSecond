from django.contrib import admin
from quickstart.models import Galaxy, StarSystem, Star, Planet, Moon


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "size_x",
        "size_y",
        "shape",
    ]


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "pos_x",
        "pos_y",
        "galaxy",
    ]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "star_system",
        "star_type",
        "diameter",
        "S",
        "age_in_centuries",
        "mass_in_suns",
    ]


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = [
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


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin):
    list_display = [
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
