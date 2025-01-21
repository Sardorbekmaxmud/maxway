# python version
FROM python:3.11.5

# python always has these next two codes
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# loyihamiz ishlashi uchun joy
WORKDIR /app

# copy python packages in this file
COPY requirements.txt /app/
# install them
RUN pip install --no-cache-dir -r requirements.txt

# app folder ga django proyektni copy qilish
COPY . /app/