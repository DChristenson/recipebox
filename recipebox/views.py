from recipebox.models import Recipe, Author
from django.shortcuts import render, HttpResponseRedirect, reverse

def index(req):
    html = "index.html"
    recipes = Recipe.objects.all()
    return render(req, html, {"data" : recipes})

def recipe_view(req, id):
    recipe_html = "recipe.html"
    recipe = Recipe.objects.filter(id=id)
    return render(req, recipe_html, {"data" : recipe})

def author_view(req, id):
    author_html = "author.html"
    author = Author.objects.filter(id=id)
    recipe = Recipe.objects.filter(author=id)
    return render(req, author_html, {"author" : author, "recipe" : recipe})


