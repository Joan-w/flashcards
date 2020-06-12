from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home view
def home(request):
    '''
    Renders home page
    '''
    return render(request, 'main/index.html')


