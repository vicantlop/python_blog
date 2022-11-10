from django.shortcuts import render

def articleList(request):
  return render(request, 'articles/articleList.html')
