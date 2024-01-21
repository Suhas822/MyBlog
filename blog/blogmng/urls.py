from django.urls import path
from .views import home,About,user_log,helps,signup,user_Dashboard,user_logout,add_blogs,update_blog,delete_blog
urlpatterns=[
    path('home/',home,name='home'),
    path('About/',About,name='About'),
    path('login/',user_log,name='login'),
    path('help/',helps,name='help'),
    path('signup/',signup,name='signup'),
    path('Dashboard/',user_Dashboard,name='Dashboard'),
    path('logout/',user_logout,name='logout'),
    path('addblog/',add_blogs,name='addblog'),
    path('updateblog/<int:id>/',update_blog,name='updateblog'),
    path('deleteblog/<int:id>/',delete_blog,name='deleteblog'),
    
]