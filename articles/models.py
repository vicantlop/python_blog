from django.db import models

# Create your models here.
# migrations - data migrated to database - we have to make a migration file
# commands to make migration file are
#   - python manage.py makemigrations
#   - python manage.py migrate

class Article(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  #add in thumbnail
  #add in author
