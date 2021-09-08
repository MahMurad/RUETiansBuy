from django.shortcuts import render
from django.http import HttpResponse

ads = [
    {
        'seller': 'Student 1',
        'title': 'Book 1',
        'category': 'Book',
        'subject': 'Introduction to web developing',
        'price': 300,
        'new': True,
        'contact_no': '01791234567',
        'date_posted': 'August 27, 2018'
    },
    {
        'seller': 'Student 2',
        'title': 'Book 2',
        'category': 'Book',
        'subject': 'Introduction to web developing 2',
        'price': 350,
        'new': True,
        'contact_no': '01791234567',
        'date_posted': 'August 27, 2018'
    }
]

# Create your views here.


def home(request):
    context = {'ads': ads}
    return render(request, 'newsfeed/home.html', context)
#, {'title': 'Home'}


def about(request):
    return render(request, 'newsfeed/about.html', {'title': 'About'})
