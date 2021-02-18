import os
import pytest
from azure.communication.phonenumbers import PhoneNumbersClient
from _shared.testcase import CommunicationTestCase, ResponseReplacerProcessor, BodyReplacerProcessor
from azure.communication.phonenumbers import PhoneNumberAssignmentType, PhoneNumberCapabilities, PhoneNumberCapabilityValue, PhoneNumberType

class NewTests(CommunicationTestCase):
    def setUp(self):
        super(NewTests, self).setUp()
        if self.is_playback():
            self.phone_number = "+18000005555"
            self.phone_number_to_release = "+18000005556"
            self.country_code = "US"
            self.area_code = "833"
        else:
            self.phone_number = os.getenv("AZURE_COMMUNICATION_SERVICE_PHONE_NUMBER")
            self.phone_number_to_release = os.getenv("AZURE_COMMUNICATION_SERVICE_PHONE_NUMBER_TO_RELEASE")
            self.country_code = os.getenv("AZURE_COMMUNICATION_SERVICE_COUNTRY_CODE")
            self.area_code = os.getenv("AZURE_COMMUNICATION_SERIVCE_AREA_CODE")
        self.phone_number_client = PhoneNumbersClient.from_connection_string(self.connection_str)
        self.recording_processors.extend([
            BodyReplacerProcessor(
                keys=[]
            ),
            ResponseReplacerProcessor(keys=[self._resource_name])])

    @pytest.mark.live_test_only
    def test_list_acquired_phone_numbers(self):
        phone_numbers = self.phone_number_client.list_acquired_phone_numbers()
        assert phone_numbers.next()
    
    @pytest.mark.live_test_only
    def test_get_phone_number(self):
        phone_number = self.phone_number_client.get_phone_number(self.phone_number)
        assert phone_number.phone_number == self.phone_number
    
    @pytest.mark.live_test_only
    def test_release_phone_number(self):
        poller = self.phone_number_client.begin_release_phone_number(self.phone_number_to_release)
        assert poller.status() == 'succeeded'

    @pytest.mark.live_test_only
    def test_search_available_phone_numbers(self):
        capabilities = PhoneNumberCapabilities(
            calling = PhoneNumberCapabilityValue.INBOUND,
            sms = PhoneNumberCapabilityValue.INBOUND_OUTBOUND
        )
        poller = self.phone_number_client.begin_search_available_phone_numbers(
            self.country_code,
            PhoneNumberType.TOLL_FREE,
            PhoneNumberAssignmentType.APPLICATION,
            capabilities,
            self.area_code,
            polling = True
        )
        assert poller.result()

    @pytest.mark.live_test_only
    def test_update_phone_number_capabilities(self):
        poller = self.phone_number_client.begin_update_phone_number_capabilities(
          self.phone_number,
          PhoneNumberCapabilityValue.OUTBOUND,
          PhoneNumberCapabilityValue.INBOUND_OUTBOUND,
          polling = True
        )
        assert poller.result()
    
    @pytest.mark.live_test_only
    def test_purchase_phone_numbers(self):
        capabilities = PhoneNumberCapabilities(
            calling = PhoneNumberCapabilityValue.INBOUND,
            sms = PhoneNumberCapabilityValue.INBOUND_OUTBOUND
        )
        search_poller = self.phone_number_client.begin_search_available_phone_numbers(
            self.country_code,
            PhoneNumberType.TOLL_FREE,
            PhoneNumberAssignmentType.APPLICATION,
            capabilities,
            self.area_code,
            1,
            polling = True
        )
        phone_number_to_buy = search_poller.result()
        purchase_poller = self.phone_number_client.begin_purchase_phone_numbers(phone_number_to_buy.search_id, polling=True)
        assert purchase_poller.result()
        release_poller = self.phone_number_client.begin_release_phone_number(phone_number_to_buy.phone_number)
        assert release_poller.status() == 'succeeded'
