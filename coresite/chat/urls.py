
from django.urls import path
from . import views
urlpatterns = [
    path('tester/', views.testView),
]
