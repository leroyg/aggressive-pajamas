import dj_database_url
import ssl

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
REDIS_URL = f"{os.environ.get('REDIS_URL', 'redis://localhost:6379/0')}?ssl_cert_reqs=none"
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
BROKER_USE_SSL = {
    'ssl_cert_reqs': ssl.CERT_NONE
}

DEBUG = False
DATABASES['default'] = dj_database_url.config(ssl_require=True)

# fix ssl mixed content issues
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# update with your site/domain
ALLOWED_HOSTS = [
    '*'
]

USE_HTTPS_IN_ABSOLUTE_URLS = True

# use whitenoise for staticfiles
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
