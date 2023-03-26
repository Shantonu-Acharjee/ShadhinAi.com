from django.contrib import admin
from .models import Slider



# for configuration fo Slider admin
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag','title', 'destination_link', 'post_date')
    search_fields = ('title', 'alt_data')



# Register your models here.
admin.site.register(Slider, SliderAdmin)
