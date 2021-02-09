import pytest
from azure.communication.administration import PhoneNumbersClient
from _shared.testcase import CommunicationTestCase, ResponseReplacerProcessor, BodyReplacerProcessor
from azure.communication.administration import PhoneNumberAssignmentType, PhoneNumberCapabilities, PhoneNumberCapabilityValue

class NewTests(CommunicationTestCase):
    def setUp(self):
        super(NewTests, self).setUp()
        self.phone_number_client = PhoneNumbersClient.from_connection_string(self.connection_str)
        self.recording_processors.extend([
            BodyReplacerProcessor(),
            ResponseReplacerProcessor(keys=[self._resource_name])])

    def test_list_acquired_phone_numbers(self):
        phone_numbers = self.phone_number_client.list_acquired_phone_numbers()
        assert phone_numbers.next()

    def test_get_phone_number(self):
        phone_number = self.phone_number_client.get_phone_number("+16194895842")
        assert phone_number.phone_number == "+16194895842"
    
    #def test_search_available_phone_numbers(self):
     #   capabilities = PhoneNumberCapabilities(
      #      calling = PhoneNumberCapabilityValue.OUTBOUND,
       #     sms = PhoneNumberCapabilityValue.NONE
       # )
        #poller = self.phone_number_client.begin_search_available_phone_numbers(
         #   "US",
          #  "tollFree",
           # PhoneNumberAssignmentType.APPLICATION,
           # capabilities,
            #"833",
        #)
        #assert poller.status() == 'succeeded'

    def test_update_phone_number_capabilities(self):
        poller = self.phone_number_client.begin_update_phone_number_capabilities(
          "+16194895842",
          PhoneNumberCapabilityValue.OUTBOUND,
          PhoneNumberCapabilityValue.OUTBOUND,
          polling = True
        )
        assert poller.status() == 'succeeded'