from .models import Category
from assignments.models import SocialLinks

def get_category(request):
    categories=Category.objects.all()

    return dict(categories=categories)

def get_sociallinks(request):
    sociallinks=SocialLinks.objects.all()

    return dict(sociallinks=sociallinks)
