from rest_framework import serializers
from yaml import serialize_all

from .models import Book, Publisher, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_price(self, price):
        if price > 5000:
            raise serializers.ValidationError('price too high')
        return price

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'