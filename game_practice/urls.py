# Manage urls for myfirstapp here
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name="homepage"), # "/" , e.g. facegame.com
    path('game', views.all_game, name='game'),
    path('game/<int:id>', views.single_game, name='single_game'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('platform/<int:id>', views.game_by_platform, name="by_platform"),
    path('upload/', views.upload_game, name='new_game'),
    path('logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path('shopping_basket/', views.shopping_basket, name="basket"),
    path('add_to_basket/<int:game_id>/', views.add_to_basket, name='add_to_basket'),
    path('add_games/', views.add_games, name="add_games")
]
