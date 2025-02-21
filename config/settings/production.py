# pylint: disable=wildcard-import, unused-wildcard-import

from .base import *  # noqa: F401

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]

STATIC_ROOT = Path("/srv/backend-static")
MEDIA_ROOT = Path("/srv/backend-media")
