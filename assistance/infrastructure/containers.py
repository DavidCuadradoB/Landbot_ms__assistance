from dependency_injector import containers, providers

from assistance.application.service.EventServiceImpl import EventServiceImpl
from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase
from assistance.infrastructure.repository.FakeEventSender import FakeEventSender


class Container(containers.DeclarativeContainer):
    event_service = providers.Factory(

        EventServiceImpl
    )

    event_sender = providers.Factory(

        FakeEventSender
    )

    request_assistance_use_case = providers.Factory(
        RequestAssistanceUseCase,
        event_sender
    )


