from django.contrib import admin
from realblog1.models import my_blog,contact_us,comments
from django.utils.html import format_html

# Register your models here.
class my_blog_admin(admin.ModelAdmin):
    list_display = ['title','date','image']
    
    def image(self,obj):
           return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    # image.allow_tags = True
class conatct_us_admin(admin.ModelAdmin):
      list_display = ['name','subject','message','email']

class comments_admin(admin.ModelAdmin):
      list_display = ['name','comm']

admin.site.register(comments,comments_admin)      
admin.site.register(contact_us,conatct_us_admin)
admin.site.register(my_blog,my_blog_admin)