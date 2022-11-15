from django.contrib import admin 
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls), #in termnal use python manage.py createsuperuser to create admin
    path('articles/', include('articles.urls')),
    path("about/", views.about),
    path('', views.home),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns() #will first check to see if we are in debug mode
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)