# Usa una imagen base con Python preinstalado
FROM python:3.9-slim

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install paramiko

# Crea un directorio para la aplicación
WORKDIR /app

# Copia el script Python al contenedor
COPY ssh_client.py /app/ssh_client.py

# Define el comando por defecto
CMD ["python", "/app/ssh_client.py"]
