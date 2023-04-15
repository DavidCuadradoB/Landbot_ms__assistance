import random
import uuid

from assistance.application.dto.AssistanceEventDTO import AssistanceEventDTO
from assistance.application.repository.EventSender import EventSender


class FakeEventSender(EventSender):
    def send_event(self, assistance_event_dto: AssistanceEventDTO):
        # TODO: Here a event should be created and it's what this service will emit to the queue. This NOT sent the
        # TODO: AssistanceEventDTO because it is a DTO.
        print("Sending event with topic %s and description %s...."
              % (assistance_event_dto.topic, assistance_event_dto.description))
        print("Event sent")
        return uuid.uuid4()
