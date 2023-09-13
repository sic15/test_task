# test_task
Тестовое задание для вакансии "Разработчик Django/Django Rest Framework"

## Описание проекта 
Каталог исполнителей и их альбомов с песнями такой структуры:
- Исполнитель
    - Название
- Альбом
    - Исполнитель
    - Год выпуска
- Песня
    - Название
    - Порядковый номер в альбоме
Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

## Стек 

- Python 3.9
- Django REST framework
- API

## Запуcк проекта: 

1) Клонировать репозиторий и перейти в него в командной строке:
git clone git@github.com:sic15/test_task.git

2) Перейти в папку catalog:
cd test_task/catalog/

3) Cоздать и активировать виртуальное окружение:
python -m venv venv 
source venv/scripts/activate

4) Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip pip install -r requirements.txt

5) Выполнить миграции:
python manage.py migrate

6) Запустить проект:
python manage.py runserver

## Об авторе 
Автор проекта Наталья Арлазарова
