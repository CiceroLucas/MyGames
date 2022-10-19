from django.urls import path

from games.views import gameList, gameView, newGame, editGame, deleteGame

urlpatterns = [
    path('', gameList, name='game-list'),
    path('game/<int:id>', gameView, name='game-view'),
    path('newgame/', newGame, name='new-game'),
    path('edit/<int:id>', editGame, name='edit-game'),
    path('delete/<int:id>', deleteGame, name='delete-game'),
]