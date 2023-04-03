from django.urls import path
from .views import signup, login_user, logout_user


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
]