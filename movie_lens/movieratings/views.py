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

def movie_details(request, movie_id):
    context = {
        "movie": Item.objects.get(id=movie_id)
    }
    return render(request, 'mov_det.html', context)
