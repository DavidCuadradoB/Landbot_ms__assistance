from assistance.application.command.RequestAssistanceCommand import RequestAssistanceCommand
from assistance.application.dto.AssistanceEventDTO import AssistanceEventDTO
from assistance.application.repository.EventSender import EventSender


class RequestAssistanceUseCase:

    def __init__(self, event_sender: EventSender):
        self.event_sender = event_sender

    def execute(self, command: RequestAssistanceCommand):
        assistance_event_dto = AssistanceEventDTO(command.topic, command.description)
        return self.event_sender.send_event(assistance_event_dto)
