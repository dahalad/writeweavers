from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Write Weavers here")

def home(request):
    context = {
        'text': 'some text',
    }

    return render(request, 'staticpage/homepage.html', context)