from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'smallsite/index.html',)


def launch_object_search(request):
    if request.POST.get('object_search_field_firstname'):
        firstname = request.POST.get('object_search_field_firstname')
        if request.POST.get('object_search_field_surname'):
            surname = request.POST.get('object_search_field_surname')
            return HttpResponse('Hello, {} {}'.format(firstname, surname))

        else:
            page = 'smallsite/index.html'
            error_message = 'Please fill the firstname and surname field'
            context = {'error_message': error_message}
            return render(request, page, context)

    else:
        page = 'smallsite/index.html'
        error_message = 'Please fill the firstname and surname field'
        context = {'error_message': error_message}
        return render(request, page, context)
