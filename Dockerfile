# Utiliza la imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al directorio de trabajo
COPY . .

# Expone el puerto que tu aplicación necesita (si aplica)
# Por ejemplo, si tu aplicación escucha en el puerto 5000
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
# Cambia "app.py" por el nombre de tu script principal o archivo de entrada
CMD ["python", "run.py"]
