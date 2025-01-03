from rest_framework import serializers
from blog.models import ArticleModel


from .models import Question, Answer

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleModel
        fields = ['id', 'image', 'title', 'description', 'author', 'created_at', 'updated_at']




class QuestionSerializer(serializers.ModelSerializer):
	answers = serializers.SerializerMethodField()
	user = serializers.StringRelatedField()


	class Meta:
		model = Question
		fields = '__all__'

	def get_answers(self, obj):
		result = obj.answers.all()
		return AnswerSerializer(instance=result, many=True).data


class AnswerSerializer(serializers.ModelSerializer):
	user = serializers.StringRelatedField()
	question = serializers.StringRelatedField()
	class Meta:
		model = Answer
		fields = '__all__'

