from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_imdb_news
from .models import *

# Create your views here.
def run_scraper(request):
    scrape_imdb_news()
    return JsonResponse({
        'status':True,
        'message': 'Scraper executed'
    }) 
    
def index(request):
    return render(request, 'index.html', context = {
        'news': News.objects.all()
     })