from django.db import models
from math import pi


class NamedEntry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name

    class Meta:
        ordering = ["name"]
        abstract = True


class SpaceBody(NamedEntry):
    diameter = models.FloatField(default=0)
    age_in_centuries = models.FloatField(default=0)
    mass_in_suns = models.FloatField(default=0)

    @property
    def S(self): return round(4 * pi * ((self.diameter / 2) ** 2), 6)

    class Meta:
        ordering = NamedEntry.Meta.ordering
        abstract = True


class Galaxy(NamedEntry):
    size_x = models.PositiveIntegerField(default=0)
    size_y = models.PositiveIntegerField(default=0)
    shape = models.CharField(max_length=10, choices=[
        ('e', 'Elliptical'),
        ('s', 'Spiral'),
        ('i', 'Irregular'),
    ], default='s')

    def __str__(self): return f"{self.name}"
    def get_absolute_url(self): return '/galaxy'


class StarSystem(NamedEntry):
    pos_x = models.PositiveIntegerField(default=0)
    pos_y = models.PositiveIntegerField(default=0)
    galaxy = models.ForeignKey("quickstart.Galaxy", on_delete=models.CASCADE, related_name="systems")


class Star(SpaceBody):
    star_system = models.ForeignKey("quickstart.StarSystem", on_delete=models.CASCADE)
    star_type = models.CharField(max_length=10, choices=[
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

    def __str__(self): return f"{self.name}"
    def get_absolute_url(self): return '/star'


class Planet(SpaceBody):
    star_system = models.ForeignKey("quickstart.StarSystem", on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    atmosphere = models.CharField(max_length=100, default='No atmosphere')
    habitable = models.BooleanField(default=False)

    def __str__(self): return f"{self.name}"
    def get_absolute_url(self): return '/planet'


class Moon(SpaceBody):
    planet = models.ForeignKey("quickstart.Planet", on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    atmosphere = models.CharField(max_length=100)
    habitable = models.BooleanField(default=False)

    def __str__(self): return f"{self.name}"
    def get_absolute_url(self): return '/moon'
