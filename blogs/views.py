from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog,Category,Comments
from django.db.models import Q
from django.http import HttpResponseRedirect


# Create your views here.

def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)

    try:    
        category=Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return redirect('home')
    context={
        'posts':posts,
        'category':category
    }

    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug)
    if request.method=='POST':
        comment=Comments()
        comment.user=request.user
        comment.blog=single_blog
        comment.comments=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments=Comments.objects.filter(blog=single_blog)
    count=comments.count()



    context={
        'single_blog':single_blog,
        'comments':comments,
        'count':count
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title__icontains=keyword)| Q(short_description__icontains=keyword)| Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html',context)
    
