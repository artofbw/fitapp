# flake8: noqa
from .settings import *

import os

SECRET_KEY = "secret_key"

DEBUG = False

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: False}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "TEST": {"NAME": os.path.join(BASE_DIR, "test.db")},
    }
}

EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

DEFAULT_FILE_STORAGE = "inmemorystorage.InMemoryStorage"
