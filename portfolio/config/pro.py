from portfolio.settings import *
import os


DEBUG = False



SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ADMINS = (
    ('kevon', 'black.king1232@gmail.com'),
    )


ALLOWED_HOSTS = ['shrouded-woodland-74637.herokuapp.com', '127.0.0.1']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = '/static/'

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"


SENDGRID_API_KEY = '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'
SENDGRID_SANDBOX_MODE_IN_DEBUG=False

EMAIL_PORT = 587
EMAIL_USE_TLS = True