from models import (
    Galaxy,
    StarSystem,
    Star,
    Planet,
    Moon
)
import random


class GeneratorGalaxy:

    def __init__(self, galaxy: Galaxy): self.galaxy = galaxy

    def check_coordinate(self, coordinates: dict):
        if self.galaxy.systems.filter(**coordinates).exists():
            print("We already have system in this coordinate")
            coordinates["pos_x"] += 10
            coordinates["pos_y"] += 10
            return self.check_coordinate(coordinates)
        return coordinates

    def generate_star_systems(self, **random_range):
        start = random_range.get("start", 0)
        end = random_range.get("end", 10000)
        self.star_system = []
        for i in range(random.randint(start, end)):
            coordinate = self.check_coordinate({
                "pos_x": random.randint(0, self.galaxy.size_x),
                "pos_y": random.randint(0, self.galaxy.size_x)
            })
            self.star_system.append(
                StarSystem.objects.create(
                    galaxy=self.galaxy,
                    name=self.galaxy.name + f" X{i}",
                    **coordinate
                )
            )
