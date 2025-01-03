from django.db import models
from django.utils.timezone import now
from accounts.models import User

def get_blog_image_filepath(self, filename):
    return f'blog/blog_images/{now().strftime("%Y/%m/%d")}/{filename}'


def get_default_blog_image():
    return 'blog/blog_default/default_blog_image.png'

class ArticleModel(models.Model):
    image = models.ImageField(upload_to=get_blog_image_filepath, default=get_default_blog_image, blank=True, null=True, verbose_name='تصویر')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن مقاله')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='articlesuser')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')
    
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def description(self):
        return {self.content[:50] + '....'}
    



class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    blog = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='questions')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.title[:20]}'

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'
        ordering = ['-created']


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.question.title[:20]}'

    class Meta:
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'
        ordering = ['-created']