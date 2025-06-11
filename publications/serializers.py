from rest_framework import serializers
from .models import Publication
from articles.serializers import ArticleSerializer

class PublicationSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'
