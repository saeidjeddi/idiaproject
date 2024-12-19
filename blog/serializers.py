from rest_framework import serializers
from blog.models import ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ArticleModel
        fields = ['id', 'image', 'title', 'description', 'author', 'created_at', 'updated_at']

    def get_image(self, obj):
        request = self.context.get('request')  
        if obj.image and obj.image.url: 
            return request.build_absolute_uri(obj.image.url)
        return request.build_absolute_uri('/media/blog/blog_default/default_blog_image.png')