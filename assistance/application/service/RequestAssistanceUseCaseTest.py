import uuid
from unittest import mock

import mockito
from django.test import TestCase
from mockito import when

from assistance import container
from assistance.application.command.RequestAssistanceCommand import RequestAssistanceCommand
from assistance.application.dto.AssistanceEventDTO import AssistanceEventDTO
from assistance.application.repository.EventSender import EventSender
from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase


# Create your tests here.
class AssistanceViewTest(TestCase):
    def test_execute_should_call_event_sender_and_return_event_uuid(self):
        a_topic = "A topic"
        a_description = "A description"
        a_uuid = uuid.uuid4()
        assistance_event_dto = AssistanceEventDTO(a_topic, a_description)
        event_sender_mock = mockito.mock(EventSender)
        when(event_sender_mock).send_event(mockito.any()).thenReturn(a_uuid)
        request_assistance_use_case = RequestAssistanceUseCase(event_sender_mock)
        request_assistance_command = RequestAssistanceCommand(a_topic, a_description)
        response = request_assistance_use_case.execute(request_assistance_command)
        self.assertEqual(response, a_uuid)
