# migrating db 
echo "migrating db..."
python manage.py migrate --no-input

# collectstatic files
echo "collectstatic files..."
python manage.py collectstatic --no-input

# runserver
echo "run gunicron server..."
#gunicorn app.wsgi:application --bind 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000

