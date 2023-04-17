import json
import pickle
import random
import uuid

from kafka import KafkaProducer

from assistance.application.dto.AssistanceEventDTO import AssistanceEventDTO
from assistance.application.repository.EventSender import EventSender


class KafkaEventSender(EventSender):
    def send_event(self, assistance_event_dto: AssistanceEventDTO):
        print('------------kafka 9093----------------')
        producer = KafkaProducer(
            bootstrap_servers=['kafka:29092'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
        event_id = uuid.uuid4()
        data = {
            'id': str(event_id),
            'topic': assistance_event_dto.topic,
            'description': assistance_event_dto.description
        }
        producer.send(assistance_event_dto.topic, value=data)

        return event_id
