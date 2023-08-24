"""
Views for the article APIs.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated

from article import serializers
from core.models import Article


class ArticleViewSet(viewsets.ModelViewSet):
    """View for manage article APIs."""
    serializer_class = serializers.ArticleDetailSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ArticleSerializer
        elif self.action == 'upload_image':
            return serializers.ArticleImageSerialzer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new article"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload_image')
    def upload_image(self, request, pk=None):
        """Upload an image to article."""
        article = self.get_object()
        serializer = self.get_serializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)