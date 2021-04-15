from django.shortcuts import render
from django.http import HttpResponse,request
from blog.models import Post,Categorie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 6)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', { 'posts': posts })

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')  

def categories(request,id):
    post_list = Post.objects.filter(category_id=id)
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request,'blog/categories.html',{ 'posts': posts })

def details(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post" : post
    }
    return render(request,'blog/post_detail.html',context)

