# zhkh
1. Установить все зависимости: pip install -r requirements.txt
2. Запустить PostgreSQL. Создать БД, применить миграции: python manage.py migrate
3. Запустить redis
4. Запустить Celery из папки zhkh_testovoye/testproj: celery -A zhkh worker -l INFO 
5. Запустить проект Django python manage.py runserver
