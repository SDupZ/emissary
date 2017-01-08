from django.shortcuts import render
from blog.models import BlogPost

def blogs_list(request):
    template = 'blogs_list.html'
    all_blogs = BlogPost.objects.all()

    context = {
        'blogs': all_blogs,
    }
    return render(request, template, context)

def blog(request, slug):
    template = 'blog.html'

    blog = BlogPost.objects.get(slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, template, context)
