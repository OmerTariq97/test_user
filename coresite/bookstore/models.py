from django.db import models

# Create your models here.
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publishere = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(default=datetime.now())


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
