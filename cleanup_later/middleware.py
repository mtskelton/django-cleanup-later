from .models import CleanupFile

class CleanupMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            CleanupFile.cleanup()
        except Exception:
            # We don't want any issues to break the user experience
            pass
        return self.get_response(request)
