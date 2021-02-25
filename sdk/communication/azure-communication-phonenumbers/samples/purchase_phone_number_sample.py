# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
<<<<<<< HEAD
<<<<<<< HEAD
FILE: purchase_phone_number_sample.py
DESCRIPTION:
    This sample demonstrates how to purchase a phone number using the search id you got from the search_available_phone_number API
USAGE:
    python purchase_phone_number_sample.py
=======
FILE: phone_number_area_codes_sample.py
=======
FILE: purchase_phone_number_sample.py
>>>>>>> cb958a482... Added fixed samples
DESCRIPTION:
    This sample demonstrates how to purchase a phone number using the search id you got from the search_available_phone_number API
USAGE:
<<<<<<< HEAD
    python list_acquired_phone_numbers_sample.py
>>>>>>> 968de8d7e... Added README and samples
=======
    python purchase_phone_number_sample.py
>>>>>>> cb958a482... Added fixed samples
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING - The endpoint of your Azure Communication Service
    2) AZURE_COMMUNICATION_SERVICE_SEARCH_ID_TO_PURCHASE - The search id for the phone number you reserved and want to purchase
"""

import os
from azure.communication.phonenumbers import (
    PhoneNumbersClient
)

connection_str = os.getenv('AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING')
<<<<<<< HEAD
<<<<<<< HEAD
search_id = os.getenv("AZURE_COMMUNICATION_SERVICE_SEARCH_ID_TO_PURCHASE")
phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_str)

def purchase_phone_number():
    poller = phone_numbers_client.begin_purchase_phone_numbers(
        search_id,
        polling = True
    )
    poller.result()
    print("Result from the purchase operation: " + poller.status())


if __name__ == '__main__':
    purchase_phone_number()
=======
phone_number = os.getenv("AZURE_COMMUNICATION_SERVICE_PHONE_NUMBER_INFORMATION")
=======
search_id = os.getenv("AZURE_COMMUNICATION_SERVICE_SEARCH_ID_TO_PURCHASE")
>>>>>>> cb958a482... Added fixed samples
phone_numbers_client = PhoneNumbersClient.from_connection_string(connection_str)

def purchase_phone_number():
    poller = phone_numbers_client.begin_purchase_phone_numbers(
        search_id,
        polling = True
    )
    poller.result()
    print("Result from the purchase operation: " + poller.status())


if __name__ == '__main__':
<<<<<<< HEAD
    get_phone_number_information()
>>>>>>> 968de8d7e... Added README and samples
=======
    purchase_phone_number()
>>>>>>> cb958a482... Added fixed samples
