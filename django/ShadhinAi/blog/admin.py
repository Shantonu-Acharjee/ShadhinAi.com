from django.contrib import admin
from .models import Slider, Post



# for configuration of Slider admin
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','title', 'destination_link', 'post_date')
    search_fields = ('title', 'alt_data')





# for configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id','image_tag','post_title', 'post_url', 'post_date')
    search_fields = ('post_title', 'post_description', 'post_short_description')






# Register your models here.
admin.site.register(Slider, SliderAdmin)
admin.site.register(Post, PostAdmin)
