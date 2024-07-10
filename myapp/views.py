from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
import random
import datetime


def index(request):
    # Example of dynamic content generation
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Innovation distinguishes between a leader and a follower. – Steve Jobs",
        "Stay hungry, stay foolish. – Steve Jobs"
    ]
    random_quote = random.choice(quotes)
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    context = {
        'quote': random_quote,
        'current_time': current_time,
    }
    return render(request, 'index.html', context)





