from django.contrib import admin
from django.urls import path
from compte.views import signup_view, login_view, profil_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name='login'),
    path('profil/', profil_view, name='profil'),
    path('logout/', logout_view, name='logout'),
]