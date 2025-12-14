from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import AddForm,AddBlogForm,AddUserForm,EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category=Category.objects.all()
    blogs=Blog.objects.all()

    context={
        'blogs':blogs,
        'category':category
    }


    return render(request,'dashboard/dashboard.html',context)

def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=AddForm()
    context={
        'form':form,
    }

    return render(request,'dashboard/add_category.html',context)

def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':
        form=AddForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=AddForm(instance=category)

    context={
        'form':form,
        'category':category
    }

    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    return render(request,'dashboard/posts.html')


def add_posts(request):
    if request.method=='POST':
        form=AddBlogForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # Temporarily saving the form
            post.author=request.user
            post.save() #then saving for generating pk/id
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id) #making the slug unique by suffixing post.id(unique) 
            post.save()
            return redirect('posts')
    else:
        form=AddBlogForm()

    context={
        'form':form
    }
    return render(request,'dashboard/add_posts.html',context)

def edit_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)

    if request.method=='POST':
        post_form=AddBlogForm(request.POST,request.FILES,instance=post)
        if post_form.is_valid():
            form=post_form.save()
            title=post_form.cleaned_data['title']
            form.slug=slugify(title)+'-'+str(form.id)
            form.save()
            return redirect('posts')
    else:
        post_form=AddBlogForm(instance=post)
    context={
        'post_form':post_form,
        'post':post

    }
    return render(request,'dashboard/edit_posts.html',context)

def delete_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users=User.objects.all()
    context={
        'users':users
    }
    return render(request,'dashboard/users.html',context)

def add_users(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=AddUserForm()

    context={
        'form':form
    }

    return render(request,'dashboard/add_users.html',context)

def edit_users(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=EditUserForm(instance=user)
    context={
        'form':form
    }
    return render(request,'dashboard/edit_users.html',context)

def delete_users(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')


        

    



