ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carwash',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

HOST = 'http://127.0.0.1:8000'
