from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import ArticleModel
from blog.serializers import ArticleSerializer
from rest_framework import status


class GetArticleApi(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True, context={'request': request})  
        return Response(serializer.data)
    

class PostArticleApi(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateArticleApi(APIView):
    def put(self, request, pk):
        article = ArticleModel.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteArticleApi(APIView):
    def delete(self, request, pk):
        article = ArticleModel.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



