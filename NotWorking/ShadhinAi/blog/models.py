from django.db import models
from django.utils.html import format_html
from base.models import BaseModel


# Create your models here.


# header model
class Header(BaseModel):
        brand_name = models.CharField(max_length= 50)
        brand_image = models.ImageField(upload_to= 'brand/')
        brand_slogan = models.CharField(max_length= 300)



class HeaderMenu(BaseModel):
    menu = models.CharField(max_length= 50)
    destination_link = models.CharField(max_length= 300)




class SubMenu(BaseModel):
     sub_menu = models.ForeignKey(HeaderMenu, on_delete= models.CASCADE, related_name='submenu')
     munu_item = models.CharField(max_length= 50)
     destination_link = models.CharField(max_length= 300)






# slider model
class Slider(BaseModel):
    image = models.ImageField(upload_to= 'slider/')
    title = models.CharField(max_length= 100)
    destination_link = models.TextField(default= '#')
    alt_data = models.CharField(max_length= 200)
    post_date = models.DateTimeField(auto_now_add= True, null= True)


    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src = "/media/{}"  style = "width: 40px; max-height: 40px;"  />'.format(self.image))







# post model
class Post(BaseModel):

    post_thumbnail = models.ImageField(upload_to= 'posts/')
    post_title = models.CharField(max_length= 200)
    post_url = models.CharField(max_length= 200, unique= True)
    post_short_description = models.CharField(max_length= 200)
    post_description = models.TextField()
    post_date = models.DateTimeField(auto_now_add= True)
    post_keyword = models.TextField()
    post_Schema = models.TextField(default='')



    def __str__(self):
        return self.post_title

    def image_tag(self):
        return format_html('<img src = "/media/{}"  style = "width: 40px; max-height: 40px;"  />'.format(self.post_thumbnail))


    