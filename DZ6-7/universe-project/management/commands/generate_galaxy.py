from django.core.management.base import BaseCommand, CommandError
from universe.models import Galaxy
from universe.galaxy_generator import GeneratorGalaxy

class Command(BaseCommand):
    help = 'Simple generator'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('size_x', type=int)
        parser.add_argument('size_y', type=int)
        parser.add_argument('min',type=int)
        parser.add_argument('max',type=int)

    def handle(self, *args, **options):
        if Galaxy.objects.filter(name=options["name"]).exists():
            raise CommandError("That universe already exist")
        galaxy = Galaxy.objects.create(
            name=options["name"],
            size_x=options["size_x"],
            size_y=options["size_y"]
        )
        generator = GeneratorGalaxy(galaxy)
        generator.generate_star_systems(start=options["min"], end=options["max"])
        self.stdout.write(self.style.SUCCESS('Hello galaxy %s' % options["name"]))
