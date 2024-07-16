# automatica_test

### Для админки:
логин: admin, 
пароль: admin

Файл .env не убирала из публичного доступа, чтобы можно было быстро проверить работоспособность проекта.

Технологии
* Python
* Django, Django REST Framework (DRF)
* PostgreSQL

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

`https://github.com/ivamari/blog_test.git`

`cd automatica_test`

### Cоздать и активировать виртуальное окружение:

`python -m venv env`

`source venv/bin/activate`

### Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

### Выполнить миграции:

`python manage.py migrate`

### Запустить проект:

`python manage.py runserver`

### Для создания суперпользователя:

`python manage.py createsuperuser`

Для перехода в админку: http://127.0.0.1:8000/admin/

Для загрузки данных в базу данных: `python manage.py loaddata data.json`

## Примеры запросов к API
Примеры запросов  в документации после запуска проекта по адресу: http://127.0.0.1:8000/api/
