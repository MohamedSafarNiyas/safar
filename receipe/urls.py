from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('createuser/',views.createuser,name='createuser'),
    path('login/',views.login,name="login"),
    path('recipe/',views.recipe,name="recipe"),

]
