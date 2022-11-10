from django.db import models

# Create your models here.
# migrations - data migrated to database - we have to make a migration file
# commands to make migration file are
#   - python manage.py makemigrations
#   - python manage.py migrate
# Django ORM - Object Relational Mapper
#   - bridges gap between code and database
#   - examples of interation include: save instance of database, retrieve models, update (CRUD)
# python and django database is SQLite

class Article(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  #add in thumbnail
  #add in author

  def __str__(self): #to look at title of objects when looking at all objects #this is a built funtion which defines how an article will look in admin section and in shell
    return self.title
  
  def snippet(self):
    return self.body[:50] + '...' # :50 up to 50 characters