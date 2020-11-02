from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')


def contact(request):
    return HttpResponse('Contact page')
