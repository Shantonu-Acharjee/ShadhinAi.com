from django.contrib import admin
from .models import Slider, Post, SubMenu, HeaderMenu, Header



# for configuration of Slider admin
class SliderAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'destination_link', 'post_date')
    search_fields = ('title', 'alt_data')





# for configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','post_title', 'post_url', 'post_date')
    search_fields = ('post_title', 'post_description', 'post_short_description')






# Register your models here.
admin.site.register(Slider, SliderAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Header)
admin.site.register(HeaderMenu)
admin.site.register(SubMenu)

