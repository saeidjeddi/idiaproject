from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import ArticleModel
from blog.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from permissions import admin


class GetArticleApi(ListAPIView):
    queryset = ArticleModel.objects.all()
    filterset_fields = ['title', 'author', 'created_at']
    ordering_fields = ['title', 'author', 'created_at']
    search_fields = ['title', 'author', 'created_at']
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination


    


class PostArticleApi(APIView):
    permission_classes = [admin.AdminPermission]

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateArticleApi(APIView):
    permission_classes = [admin.AdminPermission]
    def put(self, request, pk):
        article = ArticleModel.objects.get(id=pk)
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteArticleApi(APIView):
    permission_classes = [admin.AdminPermission]
    def delete(self, request, pk):
        article = ArticleModel.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



