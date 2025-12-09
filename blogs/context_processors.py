from .models import Category,Blog
from assignments.models import SocialLinks

def get_category(request):
    categories=Category.objects.all()

    return dict(categories=categories)

def get_blogs(request):
    blogs=Blog.objects.all()
    return dict(blogs=blogs)

def get_sociallinks(request):
    sociallinks=SocialLinks.objects.all()

    return dict(sociallinks=sociallinks)
