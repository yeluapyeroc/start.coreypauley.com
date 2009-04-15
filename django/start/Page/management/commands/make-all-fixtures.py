from django.core.management.base import NoArgsCommand
from django.core import serializers
from django.conf import settings
from start.Command.models import Basic, Advanced
from start.Bookmark.models import Bookmark

json_serializer = serializers.get_serializer('json')()

class Command(NoArgsCommand):
    help = 'Generates JSON fixtures for all the current commands'

    def handle_noargs(self, **options):
        for dir in settings.FIXTURE_DIRS:
            try:
                loc = dir + 'all-fixtures.json'
                out = open(loc, "w")
            except IOError:
                continue
            json_serializer.serialize(list(Basic.objects.all()) + list(Advanced.objects.all()) + list(Bookmark.objects.all()), stream=out)
