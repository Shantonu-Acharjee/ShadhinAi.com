from django.urls import path
from .views import signup, login_user, logout_user, profile, edit_profile, change_profile_picture, add_blog


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('add_blog/', add_blog, name='add_blog'),
]