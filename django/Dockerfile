# Usar una imagen base de Python
FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto (si tu aplicación lo necesita)
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
