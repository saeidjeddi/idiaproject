from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import ArticleModel
from blog.serializers import ArticleSerializer

class GetArticleApi(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True, context={'request': request})  
        return Response(serializer.data)