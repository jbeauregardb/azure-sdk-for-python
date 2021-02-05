import pytest
from azure.communication.administration import PhoneNumbersClient
from .phone_number_testcase import PhoneNumberCommunicationTestCase

class NewTests(PhoneNumberCommunicationTestCase):
    def test_list_acquired_phone_numbers(self):
        phone_number_client = PhoneNumbersClient.from_connection_string(self.connection_str)
        phone_numbers = phone_number_client.list_acquired_phone_numbers()
        assert phone_number_client is not None