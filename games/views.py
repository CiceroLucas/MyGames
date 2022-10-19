from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import GameForm

from .models import Game


@login_required
def gameList(request):

    search = request.GET.get('search')

    if search:
        games = Game.objects.filter(title__icontains=search, user=request.user)
    else:
        games_list = Game.objects.all().order_by('-create_at').filter(user=request.user)
        paginator = Paginator(games_list, 3)
        page = request.GET.get('page')
        games = paginator.get_page(page)

    return render(request, 'games/list.html', {'games': games})

@login_required
def gameView(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'games/game.html', {'game': game})

@login_required
def newGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        print(form)
        if form.is_valid():
            game = form.save(commit=False)
            game.done = 'doing'
            game.user = request.user
            game.save()
            messages.info(request, "Jogo salvo com sucesso.")
            return redirect('/')
    else:
        form = GameForm()
        return render(request, 'games/addgame.html', {'form': form})

@login_required
def editGame(request, id):
    game = get_object_or_404(Game, pk=id)
    form = GameForm(instance=game)

    if(request.method == 'POST'):
        form = GameForm(request.POST, instance=game)

        if(form.is_valid()):
            game.save()
            messages.info(request, "Jogo editado com sucesso.")
            return redirect('/')
        else:
            return render(request, 'games/editgame.html', {'form': form, 'game': game})
    else:
        return render(request, 'games/editgame.html', {'form': form, 'game': game})

@login_required
def deleteGame(request,id):
    game = get_object_or_404(Game, pk=id)
    game.delete()
    messages.info(request, 'Jogo deletado com sucesso.')
    return redirect('/') 