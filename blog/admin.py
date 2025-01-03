from django.contrib import admin

from blog.models import ArticleModel, Question, Answer



admin.site.register(ArticleModel)
admin.site.register(Question)
admin.site.register(Answer)
