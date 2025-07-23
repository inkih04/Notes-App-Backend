#!/bin/bash
set -e

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  echo "🔧 Creando entorno virtual..."
  python3 -m venv venv
fi

# Activar entorno virtual
echo "🔄 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias si hay requirements.txt
if [ -f "requirements.txt" ]; then
  echo "📦 Instalando dependencias desde requirements.txt..."
  pip install --upgrade pip
  pip install -r requirements.txt
fi

# Aplicar migraciones
echo "🔄 Aplicando migraciones de Django..."
python manage.py migrate
echo "✅ Migraciones aplicadas correctamente."

# Iniciar servidor
echo "🚀 Iniciando servidor de desarrollo de Django..."
python manage.py runserver 127.0.0.1:8000
