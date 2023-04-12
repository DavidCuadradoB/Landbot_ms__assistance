from django.http import HttpResponse, JsonResponse


def index(request):
    data = {
        'name': 'David',
        'location': 'Barna'
    }
    return JsonResponse(data)