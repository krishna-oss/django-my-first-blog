from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField

# Create your models here.
class my_blog(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    des = RichTextField()
    
    class Meta:
        verbose_name_plural = 'my_blog'
    
    def blog_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
    def __str__(self):
        return self.title

class contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'conatact us'
    
    def __str__(self):
      return self.name

class comments(models.Model):
   # blog1 = models.ForeignKey(my_blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    comm = models.TextField()

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.name