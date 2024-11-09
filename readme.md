# IMDb News Scraper - Celery

A a Django-based web application that scrapes the latest top news from IMDb and saves the articles to a PostgreSQL database. It uses Celery for asynchronous tasks, like downloading images, and Redis as the message broker and backend to manage task queues.


## Features:
- Web Scraping: Fetches IMDb's top news headlines, descriptions, and images.
- Celery Integration: Manages asynchronous tasks such as image downloading and database updates.
- Redis Backend: Used as a message broker and task result backend for Celery.
- Database: Stores articles and metadata in a PostgreSQL database.


## Requirements:
- Backend: Django, Celery, Redis
- Database: PostgreSQL
- Web Scraping: BeautifulSoup, Requests
- Task Queue: Celery, Redis


## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/arshaanfaraaz/IMDb-News-Scraper-Celery.git

2. Install dependencies and set up your PostgreSQL database and update the DATABASES setting in settings.py.

3. Run migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Run the Django server:
    ```bash
    python manage.py runserver

5. Start Celery:
    ```bash
    celery -A scraper worker --loglevel=info



