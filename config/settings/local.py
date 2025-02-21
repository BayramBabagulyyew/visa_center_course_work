# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

SECRET_KEY = "django-insecure-hv4&@awd3f-4dh!s@i6vmjfct00lr4j71z9dhf+)$(lwpibf)2"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # type: ignore
        "ATOMIC_REQUESTS": True,  # type: ignore
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}
CONSTANCE_REDIS_CONNECTION_CLASS = "constance.backends.memory.MemoryBackend"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_USE_SSL = False

CORS_ALLOW_ALL_ORIGINS = True

INTERNAL_IPS = ["127.0.0.1"]

# CELERY
CELERY_TASK_ALWAYS_EAGER = True
