from .models import CustomUser, Book, UserBookRating
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader

def prep_data(user):
    # Extract data from the database
    user_preferences = UserBookRating.objects.filter(user=user)

    data = {
        'user': [],
        'book': [],
        'rating': []
    }

    for preference in user_preferences:
        data['user'].append(preference.user.id)
        data['book'].append(preference.book.id)
        data['rating'].append(preference.rating)
    
    df = pd.DataFrame(data)
    return df

def train_model():
    pass

def recommend_books():
    pass