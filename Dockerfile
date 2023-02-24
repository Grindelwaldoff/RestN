FROM python:3.10-slim

RUN mkdir /app

COPY CatApi/requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY CatApi/ /app

WORKDIR /app

CMD ["gunicorn", "CatApi.wsgi:application", "--bind", "0:8000" ]