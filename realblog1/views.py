from django.shortcuts import render,redirect
from realblog1.models import my_blog,contact_us,comments
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    bl = my_blog.objects.all().order_by('-date')[:2]

    context = {
         'bl':bl
    }
    return render(request,'index.html',context)

# def blog(request):

#      my = my_blog.objects.all()
#      context = {
#           'my':my
#      }

#      return render(request, 'blog.html',context)

def contact(request):
     if request.method == 'POST':
          contact1 = contact_us()
          name = request.POST.get('name')
          email = request.POST.get('email')
          subject = request.POST.get('subject')
          message = request.POST.get('message')
          contact1.name=name
          contact1.email=email
          contact1.subject=subject
          contact1.message=message
          contact1.save()
          messages.success(request,'Thank you for contacting us')
          return render(request,'contact.html')
     else:
          return render(request,'contact.html')

def comment(request):
     if request.method == 'POST':
          comment1=comments()
          name = request.POST.get('name')
          email = request.POST.get('email')
          comment = request.POST.get('comment')
          comment1.name = name
          comment1.email = email
          comment1.comm = comment
          comment1.save()
          print('saved')
          #messages.success(request,'your comment was posted successfully')
          #return render (request,'blog.html')
     else:
          #messages.info(request,'comment was not posted please try again')
          return HttpResponse('not submitted')
          #return render (request,'blog.html')

def blog_details(request,pk):
     blog_d = my_blog.objects.get(pk=pk)

     context = {
          'bd':blog_d
     }
     return render(request,'blog.html',context)

