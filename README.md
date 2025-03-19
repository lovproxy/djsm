# Сайт стихов

Веб-приложение для публикации и чтения стихов, созданное на Django.

## Функциональность

- Просмотр каталога стихов
- Публикация собственных стихов
- Регистрация и авторизация пользователей
- Профили пользователей
- Различные категории стихов (любовная лирика, философская лирика и др.)

## Технологии

- Python 3.8+
- Django 5.0
- SQLite
- Bootstrap 5
- Crispy Forms

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш_username/djsm.git
cd djsm
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Соберите статические файлы:
```bash
python manage.py collectstatic --noinput
```

7. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Развертывание

Проект развернут на PythonAnywhere. Для развертывания на другом сервере:

1. Настройте переменные окружения
2. Измените настройки базы данных в settings.py
3. Соберите статические файлы
4. Настройте веб-сервер (например, Nginx)
5. Настройте WSGI-сервер (например, Gunicorn)

## Лицензия

MIT 