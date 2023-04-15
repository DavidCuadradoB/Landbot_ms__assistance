import http
import uuid
from unittest import mock

import mockito
from django.test import TestCase
from django.urls import reverse
from mockito import when

from assistance import container
from assistance.application.command.RequestAssistanceCommand import RequestAssistanceCommand
from assistance.application.service.RequestAssistanceUseCase import RequestAssistanceUseCase


# Create your tests here.
class AssistanceViewTest(TestCase):
    def test_post_given_a_correct_body_should_call_request_assistance_use_case(self):
        a_uuid = uuid.uuid4()
        a_topic = "A topic"
        a_description = "A description"
        dummy_request_assistance_command = RequestAssistanceCommand(a_topic, a_description)
        request_assistance_use_case = mockito.mock(RequestAssistanceUseCase)
        when(request_assistance_use_case).execute(mockito.any()).thenReturn(a_uuid)
        with container.request_assistance_use_case.override(request_assistance_use_case):
            dummyBody = {
                "topic": a_topic,
                "description": a_description
            }
            response = self.client.post(reverse("assistance"),
                                        data=dummyBody,
                                        content_type='application/json')

        self.assertContains(response, a_uuid)

    def test_post_given_an_body_without_topic_should_return_400(self):
        a_description = "A description"
        dummy_request_assistance_command = RequestAssistanceCommand("A topic", "A description")
        request_assistance_use_case = mockito.mock(RequestAssistanceUseCase)
        with container.request_assistance_use_case.override(request_assistance_use_case):
            dummyBody = {
                "description": a_description
            }
            response = self.client.post(reverse("assistance"),
                                        data=dummyBody,
                                        content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)

    def test_post_given_an_body_without_description_should_return_400(self):
        a_description = "A description"
        dummy_request_assistance_command = RequestAssistanceCommand("A topic", "A description")
        request_assistance_use_case = mockito.mock(RequestAssistanceUseCase)
        with container.request_assistance_use_case.override(request_assistance_use_case):
            dummyBody = {
                "description": a_description
            }
            response = self.client.post(reverse("assistance"),
                                        data=dummyBody,
                                        content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
