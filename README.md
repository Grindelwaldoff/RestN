# RestN

### Описание

Это бэк-енд для сайта ритуальных услуг. API предназначено исключительно для чтения. Есть возможность добавлять необходимые данные через админ панель. В рамках проекта также был произведен деплой на сервер. Ссылка на итоговый проект, в котором применялся данныйкод:

```
http://grano.col-studio.com/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Grindelwaldoff/RestN.git
```

Далее необходимо добавить файл переменных окружения с произвольными данными.

```
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
```

Далее запустить контейнер:

```
sudo docker-compose up -d
```

Провести миграции:

```
sudo docker-compose exec web python manage.py makemigrations
```

```
sudo docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
sudo docker-compose exec web python manage.py createsuperuser
```

Сайт откроется по этой ссылке:

```
http://127.0.0.1/admin/
```

#### Используемые технологии:
* Python 3.8
* Django 3.2
* PostgreSQL
* Docker
* NGINX
* Django Rest Framework
