from django.db import models
from math import pi


class NamedEntry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name

    class Meta:
        ordering = ["name"]
        abstract = True


class SpaceBody(NamedEntry):
    diameter = models.FloatField()
    age_in_centuries = models.FloatField()
    mass_in_suns = models.FloatField()
    S = diameter * pi

    class Meta:
        ordering = NamedEntry.Meta.ordering
        abstract = True


class Galaxy(NamedEntry):
    size_x = models.PositiveIntegerField()
    size_y = models.PositiveIntegerField()
    shape = models.CharField(max_length=10, choices=[
        ('e', 'Elliptical'),
        ('s', 'Spiral'),
        ('i', 'Irregular'),
    ], default='s')


class StarSystem(NamedEntry):
    name = models.CharField(max_length=50)
    pos_x = models.PositiveIntegerField()
    pos_y = models.PositiveIntegerField()
    galaxy = models.ForeignKey("universe.Galaxy", on_delete=models.CASCADE, related_name="systems")


class Star(SpaceBody):
    name = models.CharField(max_length=50)
    star_system = models.ForeignKey("universe.StarSystem", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=[
        ('bd', 'Brown Dwarf'),
        ('rd', 'Red Dwarf'),
        ('yd', 'Yellow Dwarf'),
        ('rg', 'Red Giant'),
        ('bg', 'Blue Giant'),
        ('sg', 'Supergiant'),
        ('wd', 'White Dwarf'),
        ('ns', 'Neutron Star'),
        ('p', 'Pulsar'),
        ('bh', 'Black Hole'),
        ('o', 'other'),
    ], default='yd')


class Planet(SpaceBody):
    name = models.CharField(max_length=50)
    star_system = models.ForeignKey("universe.StarSystem", on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    atmosphere = models.CharField(max_length=100)
    habitable = models.BooleanField(default=False)


class Moon(SpaceBody):
    name = models.CharField(max_length=50)
    planet = models.ForeignKey("universe.Planet", on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    atmosphere = models.CharField(max_length=100)
