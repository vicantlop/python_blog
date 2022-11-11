from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articleList, name="list"),
    path('<slug:slug>/', views.article_detail, name='detail')
]