from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name="index"),
    path('', views.login, name="login"),
]
