# IMDb News Scraper

A web scraper that fetches the latest news articles from IMDb's top stories section. It stores the news in a Django web application, which allows users to view news with details like title, description, image, and click on an external link in the title.

## Features:
- Scrapes IMDb top news.
- Saves the news articles in the Django database.
- Displays the news articles in a user-friendly interface with Bootstrap styling.
- Downloads news images and stores them locally.

## Requirements:
- Python 3.x
- Django 5.1.1
- Requests
- BeautifulSoup4
- PostgreSQL

## Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/arshaanfaraaz/IMDb-News-Scraper.git

2. Install dependencies and set up your PostgreSQL database and update the DATABASES setting in settings.py.

3. Run migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Run the Django server:
    ```bash
    python manage.py runserver


