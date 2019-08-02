# django-cleanup-later

A quick, rough around the edges Django application to remember and remove temporary files.

The purpose of this application is to allow the user to create a temporary file (e.g. for the purpose of streaming or to allow a time limited availability)
and automatically remove it after a given period of time.

At present this can be done automatically using the provided middleware, manually by running the **cleanup_later** management command, or by calling the ``CleanupFile.cleanup()`` function directly.

It's been developed and tested on Python 3.7 and Django 2.2 .. your mileage may vary with other configurations.

## Installation

Install via pip or download the repository:

```
pip install django-cleanup-later
```

Add the app to your INSTALLED_APPS setting:

```
INSTALLED_APPS = [
        ...
        'cleanup_later',
    ]
```

Make sure to migrate:

```
manage.py migrate
```

And optionally add the middleware if you want files to be removed automatically without the need for a cron or background process:

```
MIDDLEWARE = [
    ...
    'cleanup_later.middleware.CleanupMiddleware',
]
```

Note that using the middleware probably isn't the most efficient approach.  If your project is using a cron or celery for background processing, it's more efficient to run the cleanup from there.


## Usage

To use the app, simply register the filename you would like to later cleanup like so:

```
from cleanup_later.models import CleanupFile

CleanupFile.register('file_to_delete.txt')
```

By default, files will be deleted after 10 minutes, but you can override this by specifying a ``validity`` parameter as a timedelta .. e.g.

```
CleanupFile.register('file_to_delete.txt', timedelta(minutes=30))
```

Simples!


## Contributing

Pull requests are welcome if you find this library useful.
