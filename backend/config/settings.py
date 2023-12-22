from pathlib import Path
from dotenv import load_dotenv
import os
from datetime import timedelta

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
PRODUCTION = DEBUG == 0
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "::1 localhost 127.0.0.1").split()
CORS_ALLOWED_ORIGINS=os.environ.get("CORS_ALLOWED_ORIGINS", "http://localhost:3000 http://localhost:5539 http://127.0.0.1:3000").split()

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("PGSQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("PGSQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("PGSQL_USER", "user"),
        "PASSWORD": os.environ.get("PGSQL_PASSWORD", "password"),
        "HOST": os.environ.get("PGSQL_HOST", "localhost"),
        "PORT": os.environ.get("PGSQL_PORT", "5432"),
    }
}


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Importaciones de bibliotecas
    'rest_framework',
    'rest_framework_nested',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'corsheaders',
    "phonenumber_field",
    "mailqueue",
    'django_celery_beat',

    #Mis apps
    "apps.actividad",
    "apps.area",
    "apps.aseguramiento",
    "apps.local",
    "apps.medio",
    "apps.tipo_actividad",
    "apps.user",
    "apps.reservacion",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
AUTH_USER_MODEL = 'user.User'
ROOT_URLCONF = 'config.urls'



CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5539",
    "http://127.0.0.1:3000",

]

MAILQUEUE_CELERY = True
MAILQUEUE_QUEUE_UP = True
MAILQUEUE_LIMIT = 1
MAILQUEUE_STORAGE = True
MAILQUEUE_ATTACHMENT_DIR = 'mailqueue-attachments'
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", 'sentinel://sentinel-reserva:26379/0')
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'master_name': os.environ.get("CELERY_MASTER_NAME", 'mymaster'),
    'sentinels': [(os.environ.get("CELERY_SENTINEL_NAME", 'sentinel-reserva'), int(os.environ.get("CELERY_SENTINEL_PORT", 26379)))],
}
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER_URL", 'sentinel://sentinel-reserva:26379/0')
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = {
    'master_name': os.environ.get("CELERY_MASTER_NAME", 'mymaster'),
    'sentinels': [(os.environ.get("CELERY_SENTINEL_NAME", 'sentinel-reserva'), int(os.environ.get("CELERY_SENTINEL_PORT", 26379)))],
}
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = 'Cuba'
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# LDAP configuration
# -------------------------
AUTHENTICATION_BACKENDS = (
    "django_python3_ldap.auth.LDAPBackend",
    'django.contrib.auth.backends.ModelBackend',
)


AD_DNS_NAME = 'reduc.edu.cu'
AD_LDAP_PORT = 389

# LDAP Authentication Configuration

# The URL of the LDAP server.
LDAP_AUTH_URL = 'ldap://%s:%s' % (AD_DNS_NAME, AD_LDAP_PORT)

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = 'ou=CATALOGO,dc=reduc,dc=edu,dc=cu',

# The LDAP class that represents a user.
LDAP_AUTH_OBJECT_CLASS = "user"

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory_principal"
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "reduc.edu.cu"
LDAP_AUTH_SYNC_USER_RELATIONS = "apps.helper.ldap.sync_user_relations"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'Cuba'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

SWAGGER_SETTINGS = {
    'SHOW_REQUEST_HEADERS': True,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'SUPPORTED_SUBMIT_METHODS': [
        'get',
        'post',
        'put',
        'delete',
        'patch'
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=3600),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer', 'JWT', 'TOKEN'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
