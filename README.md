# practice_NPP_signal

Шаги для запуска проекта:

 - в консоли прописать: `python -m venv venv` - для создания виртуального окружения
 - `venv\Scripts\activate` - для активация виртуального окружения
 - `pip install -r requirements.txt` - для установки зависимостей
 - `python manage.py migrate` - для накатывания миграций
 -  поочередно:
    - `python manage.py loaddata fixtures/assemblies.json`
    - `python manage.py loaddata fixtures/baseProducts.json`
 - `python manage.py runserver` - для запуска проекта


## Доступные URLs

Method | URL | Description 
------|------|-------
GET | */admin* | Панель администратора

## Пользователи

Method | URL | Description 
------|------|-------
POST | *users/register* | Регистрация нового пользователя
POST | *users/login* | Авторизация пользователя
POST | *users/logout* | Разлогирование пользователя

## Основные

Method | URL | Description 
------|------|-------
GET | *assemblies* | Основное окно программы
POST | *assemblies/show-tree* | Генерация дерева изделия
POST | *assemblies/add-data* | Добавление новых компонентов
