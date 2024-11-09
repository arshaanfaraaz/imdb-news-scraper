from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_imdb_news
from .models import *
from scraper.tasks import add

# Create your views here.
def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({
        'status':True,
        'message': 'Scraper executed'
    }) 
    
def index(request):
    result = add.delay(10,20)
    print(result)
    return render(request, 'index.html', context = {
        'news': News.objects.all()
     })