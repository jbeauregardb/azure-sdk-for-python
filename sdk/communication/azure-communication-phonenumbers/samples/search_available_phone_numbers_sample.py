# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
<<<<<<< HEAD
<<<<<<< HEAD
FILE: search_available_phone_numbers_sample.py
DESCRIPTION:
    This sample demonstrates how to search for available numbers you can buy with the respective API.
USAGE:
    python search_available_phone_numbers_sample.py
=======
FILE: phone_number_area_codes_sample.py
=======
FILE: search_available_phone_numbers_sample.py
>>>>>>> cb958a482... Added fixed samples
DESCRIPTION:
    This sample demonstrates how to search for available numbers you can buy with the respective API.
USAGE:
<<<<<<< HEAD
    python list_acquired_phone_numbers_sample.py
>>>>>>> 968de8d7e... Added README and samples
=======
    python search_available_phone_numbers_sample.py
>>>>>>> cb958a482... Added fixed samples
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING - The endpoint of your Azure Communication Service
    2) AZURE_COMMUNICATION_SERVICE_AREA_CODE - The area code you want the number to be in
"""

import os
from azure.communication.phonenumbers import (
    PhoneNumbersClient,
    PhoneNumberType,
    PhoneNumberAssignmentType,
    PhoneNumberCapabilities,
<<<<<<< HEAD
    PhoneNumberCapabilityType
=======
    PhoneNumberCapabilityValue
>>>>>>> 968de8d7e... Added README and samples
)

connection_str = os.getenv('AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING')
area_code = os.getenv('AZURE_COMMUNICATION_SERVICE_AREA_CODE')
phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_str)

def search_available_phone_numbers():
    capabilities = PhoneNumberCapabilities(
<<<<<<< HEAD
        calling = PhoneNumberCapabilityType.INBOUND,
        sms = PhoneNumberCapabilityType.INBOUND_OUTBOUND
=======
        calling = PhoneNumberCapabilityValue.INBOUND,
        sms = PhoneNumberCapabilityValue.INBOUND_OUTBOUND
>>>>>>> 968de8d7e... Added README and samples
    )
    poller = phone_numbers_client.begin_search_available_phone_numbers(
        "US",
        PhoneNumberType.TOLL_FREE,
        PhoneNumberAssignmentType.APPLICATION,
        capabilities,
        area_code,
        1,
        polling = True
    )
<<<<<<< HEAD
    print('Acquired phone numbers: ' + poller.result())


if __name__ == '__main__':
    search_available_phone_numbers()
=======
    print('Acquired phone numbers:')
    print(poller.result)


if __name__ == '__main__':
<<<<<<< HEAD
    list_acquired_phone_numbers()
>>>>>>> 968de8d7e... Added README and samples
=======
    search_available_phone_numbers()
>>>>>>> cb958a482... Added fixed samples
