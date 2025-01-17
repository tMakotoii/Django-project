# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "G9p;:J|qaL(<kp|szm@M.d|!P3ZbTJ;fOb1YOJ>bh**u7SRoo=aFu6w3<CfKj'"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", '62.113.110.118',]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "super_db",
        "USER": "user_news",
        "PASSWORD": "proPARAjj333",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}