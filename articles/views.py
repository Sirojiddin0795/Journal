from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Article, Review
from .serializers import ArticleSerializer, ReviewSerializer
from .permissions import IsAuthorOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def send_to_moderator(self, request, pk=None):
        article = self.get_object()
        if article.author != request.user:
            return Response({'error': 'Ruxsat yo‘q'}, status=403)
        article.status = 'sent_to_review'
        article.save()
        return Response({'message': 'Maqola moderatorga yuborildi'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def review_result(self, request, pk=None):
        article = self.get_object()
        avg = article.avg_rating()
        if avg is not None:
            if avg >= 6:
                article.status = 'published'
            else:
                article.status = 'revision_required'
            article.save()
            return Response({'status': article.status, 'avg_rating': avg})
        return Response({'error': 'Baholar mavjud emas'}, status=400)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        article = serializer.validated_data.get('article')
        if self.request.user.profile.role != 'reviewer':
            raise PermissionError("Siz reviewer emassiz")
        serializer.save(reviewer=self.request.user)
