
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-xd@j^7&&e%-=5@ol2b9nxc)@wbot24yrelss8hb9tfpy!9gc9f'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'NAME': 'anime_db',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': 'Bekhan2005',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '854288019179-b801qvtn8fqbo6illmgcpfe2vmcj15ft.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_VK_OAUTH2_KEY = 'iXn2TL17pbw08VSu01ip'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'd370add0d370add0d370add00bd0635b1ddd370d370add0b72ae04c2ce5d23548a9dd0f'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '854288019179-b801qvtn8fqbo6illmgcpfe2vmcj15ft.apps.googleusercontent.com',
            'secret': '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',
        },
        'SCOPE': ['profile', 'email'],
    },
    'vk': {
        'APP': {
            'client_id': '51640013',
            'secret': 'iXn2TL17pbw08VSu01ip',
        },
        'SCOPE': ['email'],
    },
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1
