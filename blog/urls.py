from django.urls import path


from .views import api, template


app_name = 'blog'



urlpatterns = [
    path('', api.GetArticleApi.as_view(), name='index'),
    path('article/', api.PostArticleApi.as_view(), name='article'),
    path('article/updaete/<int:pk>/', api.UpdateArticleApi.as_view(), name='update'),
    path('article/delete/<int:pk>/', api.DeleteArticleApi.as_view(), name='delete'),
]
