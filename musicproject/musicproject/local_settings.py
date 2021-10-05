# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tpn%)^ih2j8@vwg(3-svf=gb$r(dq+t1-42@yj_!g&53!sjb%!'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'devCodeCamp',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True

        }
    }
}