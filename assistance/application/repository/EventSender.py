from abc import ABC, abstractmethod


class EventSender(ABC):

    @abstractmethod
    def send_event(self, assistance_event_dto):
        pass
