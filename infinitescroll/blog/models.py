from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField()
    author = models.CharField(max_length=30)


class Post(models.Model):
	title = models.CharField(
						max_length=200,
						verbose_name="Título de la entrada"
					)
	body = models.TextField()
	
