from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect

from recipebox.forms import Author_Input, Recipe_Input, Login_Form
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


@login_required
def add_author(req):
    html = "form.html"
    if req.user.is_staff:
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
    return HttpResponseRedirect('/error')


@login_required
def add_recipe(req):
    html = "form.html"
    if req.method == "POST":
        form = Recipe_Input(req.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = Recipe_Input()
    return render(req, html, {'form': form})


def login_view(req):
    html = "form.html"
    if req.method == "POST":
        form = Login_Form(req.POST)
        if form.is_valid():
            res = form.cleaned_data
            u = authenticate(
                username=res['username'],
                password=res['password']
            )
            if u:
                login(req, u)
                return HttpResponseRedirect(
                    req.GET.get('next', reverse('homepage'))
                )
    form = Login_Form()
    return render(req, html, {'form': form})


def logout_view(req):
    logout(req)
    return HttpResponseRedirect(reverse('homepage'))


def error_view(req):
    html = 'error.html'
    return render(req, html)
