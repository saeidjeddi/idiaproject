from django.urls import path


from .views import api, template


app_name = 'blog'


urlpatterns = [

    path('', api.GetArticleApi.as_view(), name='index')
    
]
