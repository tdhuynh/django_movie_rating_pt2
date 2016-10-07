from django.shortcuts import render

# Create your views here.
def index_view(request):

    context = {
        "top_20": "Top 20 Movies",
        "all": "All "
    }
    return render(request, 'index.html', context)

def movie_view(request):
    
    return render(request, 'index', context)
