http://127.0.0.1:8000/static/1.webp
<img src="/media/compressed/{{blog.banner}}" alt="{{blog.title}}">
{{blog.tags.all.title}}
{% for blog in blogs|slice:"6" %}
10.0.0.174:5500

<!--
        blog.category
        blog.title
        blog.user.username
        blog.created_date
        blog.blog_comments.all.count
        blog.description|truncatewords:30
        /media/blog_banners/4.webp
        blog_banners/4.webp
        -->

slider - 6
home page - 12
bloge page - 18

have to add pagenation page on sitemap.xml


video - 25done



<small>{{blog.user.username}}</small> <br>
<small>{{blog.blog_comments.all.count}} Comments</small> <br>
<small>{{blog.category.title}}</small>
pip freeze > requirements.txt



# I have t do 
- Add bangla sligify
- cheek custom slag
- if title slag is not avable avable it show to provide custom slug
- update post page tage not workong




# Comands
- python manage.py makemigrations
- python manage.py migrate