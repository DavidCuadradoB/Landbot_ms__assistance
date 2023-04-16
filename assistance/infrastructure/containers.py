from dependency_injector import containers, providers

from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase
from assistance.infrastructure.repository.FakeEventSender import FakeEventSender
from assistance.infrastructure.repository.KafkaEventSender import KafkaEventSender


class Container(containers.DeclarativeContainer):
    event_sender = providers.Factory(

        KafkaEventSender
    )

    request_assistance_use_case = providers.Factory(
        RequestAssistanceUseCase,
        event_sender
    )


