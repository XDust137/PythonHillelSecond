from django.contrib import admin
from models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin): pass


@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin): pass


@admin.register(Star)
class StarAdmin(admin.ModelAdmin): pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin): pass


@admin.register(Moon)
class MoonAdmin(admin.ModelAdmin): pass
