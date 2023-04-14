import json

from dependency_injector.wiring import inject, Provide
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from assistance.application.command.RequestAssistanceCommand import RequestAssistanceCommand
from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase
from assistance.infrastructure.containers import Container


@inject
@csrf_exempt
def assistance(request: HttpRequest,
               request_assistance_use_case: RequestAssistanceUseCase = Provide[Container.request_assistance_use_case]
               ):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))

        command = RequestAssistanceCommand(body['topic'], body['description'])

        value = request_assistance_use_case.execute(command)

        data = {
            'event': value,
        }
        return JsonResponse(data)
    else:
        data = {
            'error': 'Method Get not supported'
        }
        return JsonResponse(data)
