from dependency_injector.wiring import inject, Provide
from django.http import HttpResponse, JsonResponse, HttpRequest

from assistance.application.EventService import EventService
from assistance.infrastructure.containers import Container


@inject
def index(request: HttpRequest,
          event_service: EventService = Provide[Container.event_service]
          ):
    event_service.print_my_name()
    data = {
        'name': 'David',
        'location': 'Barna'
    }
    return JsonResponse(data)