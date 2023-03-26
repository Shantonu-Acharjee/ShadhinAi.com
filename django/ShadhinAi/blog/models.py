from django.db import models
from django.utils.html import format_html


# Create your models here.

# slider model
class Slider(models.Model):
    id = models.AutoField(primary_key= True)
    image = models.ImageField(upload_to= 'slider/')
    title = models.CharField(max_length= 100)
    destination_link = models.TextField(default= '#')
    alt_data = models.CharField(max_length= 200)
    post_date = models.DateTimeField(auto_now_add= True, null= True)


    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src = "/media/{}"  style = "width: 40px; max-height: 40px;"  />'.format(self.image))
