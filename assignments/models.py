from django.db import models

# Create your models here.


class About(models.Model):
    about_heading=models.CharField(max_length=50)
    about_description=models.TextField(max_length=255)


    def __str__(self):
        return self.about_heading
    
    class Meta:
        verbose_name_plural='About'
    

class SocialLinks(models.Model):
    platform=models.CharField(max_length=25)
    links=models.URLField()


    def __str__(self):
        return self.platform
    
    class Meta:
        verbose_name_plural='Social Links'