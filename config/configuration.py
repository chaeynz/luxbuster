ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "luxcontrol",
        "USER": "luxcontrol",
        "PASSWORD": "yourpassword",
        "HOST": "postgres",
        "PORT": "5432",
        "CONN_MAX_AGE": 300,
    }
}

SECRET_KEY = "&jkhxt#qkj%zp)jq6y4^&w(p8jeyy*c983im_8drv(fjwti@ut"

DEBUG = True
