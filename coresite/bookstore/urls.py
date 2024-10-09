"""
URL configuration for coresite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('booklistviewset', BookListViewset)
urlpatterns = [
    path('aggregate/', aggregate),
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookRetrieveView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('publishers/', PublisherListAPIView.as_view()),
    path('publishers/', PublisherListAPIView.as_view()),
    path('books_concrete/', BookListAPIView.as_view()),
    # path('books_concrete/<int:pk>', BookRetrieveAPIView.as_view()),
    path('books_concrete/<str:name>', BookRetrieveAPIView.as_view()),
    path('books_concrete/create', BookCreateAPIView.as_view()),

] + router.urls

