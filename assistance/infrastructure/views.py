from dependency_injector.wiring import inject, Provide
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from assistance.application.EventService import EventService
from assistance.infrastructure.containers import Container


@inject
@csrf_exempt
def index(request: HttpRequest,
          event_service: EventService = Provide[Container.event_service]
          ):
    print(request)
    if request.method == 'POST':
        print(request.body)
        data = {
            'name': 'Post',
        }
        return JsonResponse(data)
    else:
        event_service.print_my_name()
        data = {
            'name': 'David',
            'location': 'Barna'
        }
        return JsonResponse(data)