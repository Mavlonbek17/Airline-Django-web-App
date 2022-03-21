from django.urls import path
from .import views
urlpatterns  = [
    path("",views.index2,name = "index2"),
    path("login",views.login_views,name="login"),
    path("logout",views.logout_views,name = "logout")
]