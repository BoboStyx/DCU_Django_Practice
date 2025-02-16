from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import *
from django.contrib import messages
from . import models # models.platform, models.game
from . import forms

def index(request):
    current_user = ""
    if request.user.is_authenticated:
        current_user = request.user
    return render(request, 'index.html', {"user": current_user, "platforms" : Platform.objects.all()})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form, "platforms" : Platform.objects.all()})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form, "platforms" : Platform.objects.all()})

def all_game(request):
    game = models.Game.objects.all()
    return render(request,'game.html', {'game':game, "platforms" : Platform.objects.all()})


def single_game(request, id):
    #game = models.game.objects.get(id=id)
    game = get_object_or_404(models.Game, pk=id)
    # if game is None
    # return 404 page
    # else
    # return product page
    return render(request, 'game_individual.html', {'game':game, "platforms" : Platform.objects.all()})

def game_by_platform(request, id):
    platform = get_object_or_404(models.Platform, pk=id)
    game = models.Game.objects.filter(Game_Platform=platform)
    return render(request, 'platform.html', {'platform':platform, 'game': game, "platforms" : Platform.objects.all()})



def upload_game(request):
        if request.user.is_superuser:
        # if user us performing GET reuqest, show the form
        # if user is performing post request, 
        # the user has submitted the form and we need to save the data
        
            if request.method == "POST":
                form = forms.GameForm(request.POST) # Create a game with the data sent in the POST request
                if form.is_valid():
                    game = form.save() # Create a new game object and save it in the database
                    return render(request, 'game_individual.html', {'game':game, "platforms" : Platform.objects.all()}) # bounce user to the single game page
            else:
                # Just show the form
                form = forms.GameForm()
            return render(request, 'upload_game.html', {'form':form, "platforms" : Platform.objects.all()})
        else:
            return redirect('homepage')

def add_games(request):
    game = models.Game.objects.all()
    return render(request, 'add_games.html', {'games': game, "platforms" : Platform.objects.all()})

def add_to_basket(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if game.Number_In_Stock > 0:
        basket, created = Cart.objects.get_or_create(user=request.user)

        # Add game to cart
        basket.game.add(game)

        game.Number_In_Stock -= 1
        game.save()

        messages.success(request, f"{game.Name} has been added to your basket!")
        return redirect('basket')
    else:
        messages.error(request, f"{game.Name} is out of stock!")
    return redirect('add_games')


def shopping_basket(request):
    basket, creation = Cart.objects.get_or_create(user=request.user)
    All_games = basket.game.all()
    return render(request, 'shopping_basket.html', {"basket": basket, 'games' : All_games, "platforms" : Platform.objects.all()})

