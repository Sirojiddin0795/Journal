from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Requirement
from .serializers import RequirementSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all().order_by('-created_at')
    serializer_class = RequirementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
