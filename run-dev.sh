set -e

echo "🔄 Aplicando migraciones de Django..."
python manage.py migrate --noinput

echo "✅ Migraciones aplicadas correctamente."

echo "🚀 Iniciando Gunicorn..."
gunicorn notes_backend.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 4 \
    --timeout 120


