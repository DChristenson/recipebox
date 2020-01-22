from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect

from recipebox.forms import Author_Input, Recipe_Input
from recipebox.models import Recipe, Author


def index(req):
    html = "index.html"
    recipes = Recipe.objects.all()
    return render(req, html, {"data": recipes})


def recipe_view(req, id):
    recipe_html = "recipe.html"
    recipe = Recipe.objects.filter(id=id)
    return render(req, recipe_html, {"data": recipe})


def author_view(req, id):
    author_html = "author.html"
    author = Author.objects.filter(id=id)
    recipe = Recipe.objects.filter(author=id)
    return render(req, author_html, {"author": author, "recipe": recipe})


def add_author(req):
    html = "form.html"
    if req.method == "POST":
        form = Author_Input(req.POST)
        if form.is_valid():
            res = form.cleaned_data
            u = User.objects.create(
                username=res['user'],
                password=res['password']
            )
            Author.objects.create(
                user=u,
                name=res['name'],
                body=res['body']
            )
        return HttpResponseRedirect(reverse('homepage'))
    form = Author_Input()
    return render(req, html, {'form': form})


def add_recipe(req):
    html = "form.html"
    if req.method == "POST":
        form = Recipe_Input(req.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = Recipe_Input()
    return render(req, html, {'form': form})
