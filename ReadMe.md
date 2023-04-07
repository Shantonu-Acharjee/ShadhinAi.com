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
- only admin can post user can comment user post should be aproveable
- comment section link will not follow/working
- I can't follow myself
- have to add most view post / most propular post
- have to create notificashon for comments
- i have to use page not found 
- i have to use custom sitemap.xml
- tag is not editable problem solve
- forgot password






# Comands
- python manage.py makemigrations
- python manage.py migrate
- python manage.py startapp notification
- virtualenv env
- pip install django
- pip install pillow
- pip install django-ckeditor
- pip freeze > requirements.txt
- pip3.8 install --user pythonanywhere
- python manage.py createsuperuser
- Shantonu560634
- https://www.pythonanywhere.com/user/ShantonuAcharjee/consoles/28165668/