from django.urls import path, include
from comms import views as comms_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", comms_views.mainPage, name="main-page"),

    path("auth/login/",
         LoginView.as_view(template_name="comms/loginPage.html"),
         name="login-user"),
    
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]