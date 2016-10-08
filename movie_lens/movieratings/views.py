from django.shortcuts import render
from movieratings.models import Item, Rater, Data

# Create your views here.
def index_view(request):
    context = {
        "top_20": "Top 20 Movies",
        "all_mov": "All Movies",
        'all_rate': "All Raters"
    }
    return render(request, 'index.html', context)


def top_mov_view(request):
    context = {
        "top": "filler stuffz"
    }
    return render(request, 'top_mov.html', context)

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
