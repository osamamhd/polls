from django.contrib.auth import views
from  django.urls import path
from users.forms import UserLoginForm
from users.views import signup_view

urlpatterns = [

    path(
        'login/',
        views.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
    ),

    path(
        'signup/',
        signup_view,
        name='signup'
    ),
    
]