from django.shortcuts import render
from movieratings.models import Item, Rater, Data
from django.db.models import Avg


def index_view(request):
    context = {
        "top": "Top 20 Rated Movies",
        "all_mov": "All Movies",
        'all_rate': "All Raters"
    }
    return render(request, 'index.html', context)


def top_movies_view(request):
    context = {
        "top_movies": Item.objects.annotate(top_20=Avg('data__rating')).order_by('-top_20')[:20],
    }
    return render(request, 'top_movies.html', context)


def movie_view(request):
    context = {
        "all_movies": Item.objects.all(),
    }
    return render(request, 'movies.html', context)


def rater_view(request):
    context = {
        "all_raters": Rater.objects.all()
    }
    return render(request, 'raters.html', context)


def movie_detail(request, movie_id):
    context = {
        "movie": Item.objects.get(id=movie_id),
        "rater_of_movie": Data.objects.filter(item=movie_id)
    }
    return render(request, 'movie_detail.html', context)


def rater_detail(request, rater_id):
    context = {
        "rater": Rater.objects.get(id=rater_id),
        "movies_rated": Data.objects.filter(rater=rater_id)

    }
    return render(request, 'rater_detail.html', context)
