from django.db import models
from django.utils.text import slugify

class Slider(models.Model):
    title = models.CharField(max_length= 150)
    banner = models.ImageField(upload_to = 'slider')
    slug = models.SlugField(null= True, blank= True)
    destination = models.CharField(max_length= 250, default= '#')
    created_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
         self.slug = slugify(self.title)
         super().save(*args, **kwargs)
