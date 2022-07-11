web: gunicorn users_api.wsgi
release: python manage.py makgemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
