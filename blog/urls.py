from django.urls import path


from .views import api


app_name = 'blog'



urlpatterns = [
    path('', api.GetArticleApi.as_view(), name='index'),
    path('article/', api.PostArticleApi.as_view(), name='article'),
    path('article/updaete/<int:pk>/', api.UpdateArticleApi.as_view(), name='update'),
    path('article/delete/<int:pk>/', api.DeleteArticleApi.as_view(), name='delete'),
]


urlpatterns += [

    path('questions/', api.QuestionListView.as_view()),
	path('question/create/', api.QuestionCreateView.as_view()),
	path('question/update/<int:pk>/', api.QuestionUpdateView.as_view()),
	path('question/delete/<int:pk>/', api.QuestionDeleteView.as_view()),

]