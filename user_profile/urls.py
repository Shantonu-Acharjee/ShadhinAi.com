from django.urls import path
from .views import signup, login_user, logout_user, profile, edit_profile, change_profile_picture, add_blog, update_blog, view_user_information, follow_or_unfollow_user


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path('view_user_information/<str:username>/', view_user_information, name='view_user_information'),
    path('follow_or_unfollow/<int:user_id>/', follow_or_unfollow_user, name= 'follow_or_unfollow_user')
]