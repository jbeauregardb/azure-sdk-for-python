# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class BillingFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The frequency with which the cost gets billed.
    """

    MONTHLY = "monthly"

class PhoneNumberAssignmentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The assignment type of the phone numbers to search for. A phone number can be assigned to a
    person, or to an application.
    """

    USER = "user"
    APPLICATION = "application"

class PhoneNumberCapabilityValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Capability value for calling.
    """

    NONE = "none"
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    INBOUND_OUTBOUND = "inbound+outbound"

class PhoneNumberOperationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of operation.
    """

    NOT_STARTED = "notStarted"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

class PhoneNumberOperationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of operation, e.g. Search
    """

    PURCHASE = "purchase"
    RELEASE_PHONE_NUMBER = "releasePhoneNumber"
    SEARCH = "search"
    UPDATE_PHONE_NUMBER_CAPABILITIES = "updatePhoneNumberCapabilities"

class PhoneNumberType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of phone numbers to search for, e.g. geographic, or tollFree.
    """

    GEOGRAPHIC = "geographic"
    TOLL_FREE = "tollFree"
