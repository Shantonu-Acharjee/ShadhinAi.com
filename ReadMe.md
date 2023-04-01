http://127.0.0.1:8000/static/1.webp
<img src="/media/compressed/{{blog.banner}}" alt="{{blog.title}}">
{{blog.tags.all.title}}
{% for blog in blogs|slice:"6" %}


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


video - 8 done