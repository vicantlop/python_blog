from django.shortcuts import render
from .models import Article

def articleList(request):
  articles = Article.objects.all().order_by('date') #order_by allows us to order objects by any variable in the model
  return render(request, 'articles/articleList.html', {'articles': articles})
