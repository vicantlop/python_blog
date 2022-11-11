from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def articleList(request):
  articles = Article.objects.all().order_by('date') #order_by allows us to order objects by any variable in the model
  return render(request, 'articles/articleList.html', {'articles': articles})

def article_detail(request, slug):
  # return HttpResponse(slug)
  article = Article.objects.get(slug=slug)
  return render(request, 'articles/article_detail.html', { 'article': article })