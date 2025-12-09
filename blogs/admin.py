from django.contrib import admin
from . models import Category,Blog,Comments
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','category','created_at','updated_at','status','is_featured']
    search_fields=['id','status','title','category__category_name']

admin.site.register(Category)
admin.site.register(Blog,BlogAdmin) 
admin.site.register(Comments)
