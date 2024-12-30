from rest_framework import serializers
from blog.models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleModel
        fields = ['id', 'image', 'title', 'content', 'author', 'created_at', 'updated_at']

