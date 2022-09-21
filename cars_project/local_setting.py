# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5lfldsohj=r3l#uo@sk5j9=ckn3a^5l)s0@&3xdj-_&mu)d5jz"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
