from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.permissions import AllowAny

class MainPageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        last_edition = Article.objects.filter(status='published').order_by('-created_at').first()
        last_papers = Article.objects.filter(status='published').order_by('-created_at')[:4]
        most_read = Article.objects.filter(status='published').order_by('-views')[:8]

        data = {
            "last_edition": ArticleSerializer(last_edition, context={'request': request}).data if last_edition else None,
            "last_papers": ArticleSerializer(last_papers, many=True, context={'request': request}).data,
            "most_read": ArticleSerializer(most_read, many=True, context={'request': request}).data
        }
        return Response(data)
