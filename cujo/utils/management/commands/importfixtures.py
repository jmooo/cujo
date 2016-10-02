import os
from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.conf import settings

class Command(BaseCommand):
    help = 'Imports a list of fixtures in order'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR

        management.call_command("flush")

        fixtures = [
            # os.path.join(base_dir, "apps/some_app/fixtures/initial.json"),
        ]

        for fixture in fixtures:
            management.call_command("loaddata", fixture)

        print "Done!"
