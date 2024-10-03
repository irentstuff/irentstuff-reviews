import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-r!ye3(+uevi2$d%t$qam%8o829&fgd%5h_57-itp&#cx++^3p-"
DEBUG = True
ALLOWED_HOSTS = [
    "0.0.0.0",
    "13.213.70.177",
    "localhost",
    "ec2-13-213-70-177.ap-southeast-1.compute.amazonaws.com",
    "127.0.0.1",
    "ec2-47-128-254-114.ap-southeast-1.compute.amazonaws.com",
]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reviews",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_cognito_jwt",
    "django_prometheus",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = "irentstuff_reviews.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "irentstuff_reviews.wsgi.application"


# # Determine the environment
# ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

# # Database configuration
# if ENVIRONMENT == 'production':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'reviews',  # Your MySQL database name
#             'USER': 'admin',  # Your MySQL username
#             'PASSWORD': 'mtech111',  # Your MySQL password
#             'HOST': 'reviewsdb.cpqym0scccor.ap-southeast-1.rds.amazonaws.com',  # Your RDS host
#             'PORT': '3306',
#             'OPTIONS': {
#                 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#             }
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": "reviews",  # The database name in MySQL
        "USER": "admin",  # Your RDS username
        "PASSWORD": "mtech111",  # Your RDS password
        "HOST": "reviewsdb.cpqym0scccor.ap-southeast-1.rds.amazonaws.com",  # Your RDS endpoint
        "PORT": "3306",
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "django_cognito_jwt.JSONWebTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
}


PROMETHEUS_EXPORT_MIGRATIONS = False 