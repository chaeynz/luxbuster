cd luxcontrol

gunicorn luxcontrol.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 1 \
  --timeout 120
