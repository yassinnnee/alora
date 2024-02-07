from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def pricing(request):
    return render(request, 'pricing.html',{})

def about(request):
    return render(request, 'about.html',{})

def blog_home(request):
    return render(request, 'blog-home.html',{})

def blog_post(request):
    return render(request, 'blog-post.html',{})

def faq(request):
    return render(request,'faq.html',{})
