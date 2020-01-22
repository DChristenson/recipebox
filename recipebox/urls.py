"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipebox import views, models

admin.site.register(models.Author)
admin.site.register(models.Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipes/<int:id>/', views.recipe_view, name='recipepage'),
    path('author/<int:id>/', views.author_view, name='authorpage'),
    path('addauthor/', views.add_author, name='addauthor'),
    path('addrecipe/', views.add_recipe, name='addrecipe')
]