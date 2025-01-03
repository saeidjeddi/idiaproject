from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import ArticleModel
from blog.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from permissions import admin


from ..models import Question
from ..serializers import QuestionSerializer

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




class QuestionListView(APIView):

	def get(self, request):
		questions = Question.objects.all()
		srz_data = QuestionSerializer(instance=questions, many=True).data
		return Response(srz_data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):

	serializer_class = QuestionSerializer

	def post(self, request):
		srz_data = QuestionSerializer(data=request.data)
		if srz_data.is_valid():
			srz_data.save()
			return Response(srz_data.data, status=status.HTTP_201_CREATED)
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):

	def put(self, request, pk):
		question = Question.objects.get(pk=pk)
		self.check_object_permissions(request, question)
		srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
		if srz_data.is_valid():
			srz_data.save()			
			return Response(srz_data.data, status=status.HTTP_200_OK)
		return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):

	def delete(self, request, pk):
		question = Question.objects.get(pk=pk)
		question.delete()
		return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)