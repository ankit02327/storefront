from .common import *
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront2",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}


DEBUG = True

MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]

SECRET_KEY = "django-insecure-^w88g%c_cq9p^mcqq!4@=4v(y6l^07oub2in5u3o#m+va9%grm"
