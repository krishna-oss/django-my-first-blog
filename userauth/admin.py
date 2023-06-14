from django.contrib import admin
from userauth.models import User
# Register your models here.
class User_admin(admin.ModelAdmin):
    list_display = ['username','email','phone_number']

admin.site.register(User,User_admin)