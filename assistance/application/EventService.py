from abc import ABC, abstractmethod


class EventService(ABC):

    @abstractmethod
    def print_my_name(self):
        pass
