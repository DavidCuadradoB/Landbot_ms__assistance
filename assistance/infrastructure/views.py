import json

from dependency_injector.wiring import inject, Provide
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from assistance.application.command.RequestAssistanceCommand import RequestAssistanceCommand
from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase
from assistance.infrastructure.containers import Container


@inject
@csrf_exempt
def assistance(request: HttpRequest,
               request_assistance_use_case: RequestAssistanceUseCase = Provide[Container.request_assistance_use_case]
               ):
    # TODO: This is weird, Investigate if there are a better way to access only the post.
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        try:
            command = RequestAssistanceCommand(body['topic'], body['description'])
        except KeyError as e:
            return HttpResponseBadRequest('The body should contain a topic and a description')

        value = request_assistance_use_case.execute(command)
        data = {
            'event': value,
        }
        return JsonResponse(data)
