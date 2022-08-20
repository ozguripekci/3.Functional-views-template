from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print(request.user)
    html = "<h1>Hello from Views!</h1>"
    return HttpResponse(html)


def special(request):
    context = {
        'title': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list':[2,3,4]
    }
    return render(request, 'app/special.html', context)