from .models import Category, Tag

def get_all_categories(request):
    categories = Category.objects.all()
    context ={
        "categories" : categories
    }

    return context




def get_all_tags(request):
    tags = Tag.objects.all()
    context ={
        "tags" : tags
    }

    return context
