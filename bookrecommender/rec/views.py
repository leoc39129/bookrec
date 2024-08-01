from django.shortcuts import render
from .models import CustomUser, Movie, UserMovieRating
from .train import prep_data, train_model, recommend_books

# Create your views here.
def index(request):
    return render(request, 'templates/index.html')

def quiz(request):
    if request.method == 'POST':
        # Save user data
        pass
    return render(request, 'templates/quiz.html')

def results(request):
    # Generate and display book recommendations
    user = request.data.get('user')

    # Find details of the following functions in train.py
    df = prep_data(user)
    model = train_model(df)
    recommendations = recommend_books(model) 

    return render(request, 'templates/results.html', {'recommendations': recommendations})


    
