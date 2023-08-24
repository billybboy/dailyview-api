"""
Serializers for article APIs
"""
from rest_framework import serializers

from core.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for articles."""

    class Meta:
        model = Article
        fields = ['id', 'title', 'date', 'image']


class ArticleDetailSerializer(ArticleSerializer):
    """Serializer for article detail view."""

    class Meta(ArticleSerializer.Meta):
        fields = ArticleSerializer.Meta.fields


class ArticleImageSerialzer(serializers.ModelSerializer):
    """Serializer for uploading images to articles."""

    class Meta:
        model = Article
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': True}}