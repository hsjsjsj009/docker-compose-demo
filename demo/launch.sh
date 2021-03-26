python manage.py makemigrations
python manage.py migrate
gunicorn --bind :"$PORT" demo.wsgi