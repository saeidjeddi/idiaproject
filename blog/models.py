from django.db import models
from django.utils.timezone import now


def get_blog_image_filepath(self, filename):
    return f'blog/blog_images/{now().strftime("%Y/%m/%d")}/{filename}'


def get_default_blog_image():
    return 'blog/blog_default/default_blog_image.png'

class ArticleModel(models.Model):
    image = models.ImageField(upload_to=get_blog_image_filepath, default=get_default_blog_image, blank=True, null=True, verbose_name='تصویر')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    content = models.TextField(verbose_name='متن مقاله')
    author = models.CharField(max_length=50, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def description(self):
        return self.content[:5]