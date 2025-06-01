from rest_framework import serializers
from .models import Category, Term, SearchLog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TermSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Term
        fields = '__all__'

class SearchLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchLog
        fields = '__all__'
