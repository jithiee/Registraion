
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signuppage,name='singup'),
    path('login/',views.Loginpage,name='login'),
    path('home/',views.Homepage,name='home'),
    
]
