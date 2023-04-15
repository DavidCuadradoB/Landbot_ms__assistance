from abc import ABC, abstractmethod

from assistance.application.dto.AssistanceEventDTO import AssistanceEventDTO


class EventSender(ABC):

    @abstractmethod
    def send_event(self, assistance_event_dto: AssistanceEventDTO):
        pass
