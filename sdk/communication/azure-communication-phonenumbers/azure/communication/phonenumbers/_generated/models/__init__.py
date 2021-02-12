# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AcquiredPhoneNumber
    from ._models_py3 import AcquiredPhoneNumbers
    from ._models_py3 import CommunicationError
    from ._models_py3 import CommunicationErrorResponse
    from ._models_py3 import PhoneNumberCapabilities
    from ._models_py3 import PhoneNumberCapabilitiesRequest
    from ._models_py3 import PhoneNumberCost
    from ._models_py3 import PhoneNumberOperation
    from ._models_py3 import PhoneNumberPurchaseRequest
    from ._models_py3 import PhoneNumberSearchRequest
    from ._models_py3 import PhoneNumberSearchResult
except (SyntaxError, ImportError):
    from ._models import AcquiredPhoneNumber  # type: ignore
    from ._models import AcquiredPhoneNumbers  # type: ignore
    from ._models import CommunicationError  # type: ignore
    from ._models import CommunicationErrorResponse  # type: ignore
    from ._models import PhoneNumberCapabilities  # type: ignore
    from ._models import PhoneNumberCapabilitiesRequest  # type: ignore
    from ._models import PhoneNumberCost  # type: ignore
    from ._models import PhoneNumberOperation  # type: ignore
    from ._models import PhoneNumberPurchaseRequest  # type: ignore
    from ._models import PhoneNumberSearchRequest  # type: ignore
    from ._models import PhoneNumberSearchResult  # type: ignore

from ._phone_numbers_client_enums import (
    BillingFrequency,
    PhoneNumberAssignmentType,
    PhoneNumberCapabilityValue,
    PhoneNumberOperationStatus,
    PhoneNumberOperationType,
    PhoneNumberType,
)

__all__ = [
    'AcquiredPhoneNumber',
    'AcquiredPhoneNumbers',
    'CommunicationError',
    'CommunicationErrorResponse',
    'PhoneNumberCapabilities',
    'PhoneNumberCapabilitiesRequest',
    'PhoneNumberCost',
    'PhoneNumberOperation',
    'PhoneNumberPurchaseRequest',
    'PhoneNumberSearchRequest',
    'PhoneNumberSearchResult',
    'BillingFrequency',
    'PhoneNumberAssignmentType',
    'PhoneNumberCapabilityValue',
    'PhoneNumberOperationStatus',
    'PhoneNumberOperationType',
    'PhoneNumberType',
]
