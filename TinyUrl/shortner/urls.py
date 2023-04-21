from django.urls import path,include
from . views import SignUp,LogIn,Home,Profile,CreateUrl,Jump,LogOut,DeleteUrl

app_name = 'shortner'
urlpatterns = [
    path('',LogIn,name="login"),
    path('signup/',SignUp,name="signup"),
    path('logout/',LogOut,name="logout"),
    path('home/', Home,name="home"),
    path('profile/',Profile,name="profile"),
    path('create/', CreateUrl,name="create_url"),
    path('<str:pk>', Jump,name="jump"),
    path('delete/<int:pk>', DeleteUrl,name="delete"),
]