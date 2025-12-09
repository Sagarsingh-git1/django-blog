from django import forms
from blogs.models import Category,Blog
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class AddBlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','short_description','blog_body','featured_image','status','category','is_featured')

class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')

class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','is_active','is_staff','is_superuser','groups','user_permissions')