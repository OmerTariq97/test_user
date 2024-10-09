from logging import raiseExceptions

from rest_framework.response import Response
from twisted.names.client import query
from yaml import serialize

from .models import *
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .serializer import BookSerializer, PublisherSerializer, AuthorSerializer
from rest_framework import viewsets
# Create your views here.
def aggregate(request):
    # Booking.objects
    # publisher_instance = Publisher.objects.create(name='omer_pub')
    # author1 = Author.objects.create(name='omer',age=35)
    # author2 = Author.objects.create(name='omer',age=35)
    # author3 = Author.objects.create(name='omer',age=35)
    # book_instance = Book.objects.create(name='book_1', pages='50', price=32, rating=4, publishere=publisher_instance)
    # book_instance1 = Book.objects.create(name='book_1', pages='50', price=7777, rating=1, publishere=publisher_instance)
    # book_instance2 = Book.objects.create(name='book_1', pages='50', price=5000, rating=2, publishere=publisher_instance)
    # book_instance.authors.set([author1, author2])
    # book_instance1.authors.set([author1, author2, author3])
    # store1 = Store.objects.create(name='store1')
    # store2 = Store.objects.create(name='store1')
    # store1.books.set([book_instance, book_instance1])
    # store2.books.set([book_instance, book_instance1])
    # x = Publisher.objects.annotate(Count('book'))
    # print(x.values)
    # Book.objects.select_related('publishere')

    # select_related understanding
    # queryset = Book.objects.all()
    # for q in queryset:
    #     print(q.publishere)
    # queryset = Book.objects.select_related('publishere')
    # for q in queryset:
    #     print(q.publishere)

    # prefetch related undestanding
    # book_queryset = Book.objects.all()
    # book_queryset = Book.objects.prefetch_related('authors')
    # for book in book_queryset:
    #     for author in book.authors.all():
    #         a = author

    # prefetch on foreign key to understand sql query
    publishers = Publisher.objects.prefetch_related('book_set').all()
    for publisher in publishers:
        print(publisher.book_set)

    return render(request, 'bookstore1.html')

class BookListView(GenericAPIView, ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

class BookListViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class BookCreateView(GenericAPIView, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request)

class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.filter(price=7777.00)
    serializer_class = BookSerializer

    # works as intended (gives error on Author because of different fields which is how it should work)
    # def get_serializer_class(self):
    #     # return PublisherSerializer
    #     return AuthorSerializer
    #
    # def get(self, request):
    #     # queryset = Book.objects.filter(price=5000)
    #     queryset = self.get_queryset()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)

class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'name'

    # get_object works together with lookup_field to retrieve a object
    def get_object(self):
        name = self.kwargs.get('name')
        return Book.objects.get(name=name)

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)