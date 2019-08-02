from django.core.management.base import BaseCommand

from cleanup_later.models import CleanupFile

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        CleanupFile.cleanup()
