from rest_framework import serializers
from .models import Article, Review

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('status', 'author')

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('reviewer', 'article')
