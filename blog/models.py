from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
      title = models.CharField(max_length=200)

      def __str__(self):
          return self.title

class Post(models.Model):
    category = models.ForeignKey(Categorie, verbose_name="category",on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    body    = models.TextField()
    author    = models.CharField(max_length=255)
    post_date    = models.DateTimeField()
