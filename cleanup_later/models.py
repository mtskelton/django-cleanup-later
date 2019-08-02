import datetime
import os

from django.db import models
from django.utils import timezone


class CleanupFile(models.Model):
    filename = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    cleanup_after = models.DateTimeField()

    @classmethod
    def register(cls, filename, validity=None):
        if validity and not isinstance(validity, datetime.timedelta):
            raise Exception('validity must be a timedelta')

        cleanup_after = timezone.now() + datetime.timedelta(minutes=10) if not validity else timezone.now() + validity

        cls(filename=filename,
            cleanup_after=cleanup_after).save()

    @classmethod
    def cleanup(cls):
        for cf in cls.objects.filter(cleanup_after__lt=timezone.now()):
            if os.path.exists(cf.filename):
                os.remove(cf.filename)

            cf.delete()
