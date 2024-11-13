from django.shortcuts import render

def blog_handler(request):
    context = {}
    return render(request, 'news/blog.html', context)

def about_handler(request):
    context = {}
    return render(request, 'news/about.html', context)

def contact_handler(request):
    context = {}
    return render(request, 'news/contact.html', context)

def page_handler(request):
    context = {}
    return render(request, 'news/post-details.html', context)

def index_handler(request):
    context = {}
    return render(request, 'news/index.html', context)

def robots_handler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')