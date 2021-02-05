# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._phone_numbers_client_enums import *


class AcquiredPhoneNumber(msrest.serialization.Model):
    """Represents an acquired phone number.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The id of the phone number, e.g. 11234567890.
    :type id: str
    :param phone_number: Required. String of the E.164 format of the phone number, e.g.
     +11234567890.
    :type phone_number: str
    :param country_code: Required. The ISO 3166-2 code of the phone number's country, e.g. US.
    :type country_code: str
    :param phone_number_type: Required. The phone number's type, e.g. Geographic, TollFree.
     Possible values include: "geographic", "tollFree".
    :type phone_number_type: str or ~azure.communication.administration.models.PhoneNumberType
    :param capabilities: Required. Capabilities of a phone number.
    :type capabilities: ~azure.communication.administration.models.PhoneNumberCapabilities
    :param assignment_type: Required. The assignment type of the phone number. A phone number can
     be assigned to a person, or to an application. Possible values include: "user", "application".
    :type assignment_type: str or
     ~azure.communication.administration.models.PhoneNumberAssignmentType
    :param purchase_date: The date and time that the phone number was purchased.
    :type purchase_date: ~datetime.datetime
    :param callback_uri: The webhook for receiving incoming events, e.g. https://{{site-
     name}}.azurewebsites.net/api/updates.
    :type callback_uri: str
    :param application_id: The application id of the server application the phone number is
     assigned to. The property is empty if the phone number is assigned to a person.
    :type application_id: str
    :param cost: Required. The incurred cost for a single phone number.
    :type cost: ~azure.communication.administration.models.PhoneNumberCost
    """

    _validation = {
        'id': {'required': True},
        'phone_number': {'required': True},
        'country_code': {'required': True},
        'phone_number_type': {'required': True},
        'capabilities': {'required': True},
        'assignment_type': {'required': True},
        'cost': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'purchase_date': {'key': 'purchaseDate', 'type': 'iso-8601'},
        'callback_uri': {'key': 'callbackUri', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'cost': {'key': 'cost', 'type': 'PhoneNumberCost'},
    }

    def __init__(
        self,
        *,
        id: str,
        phone_number: str,
        country_code: str,
        phone_number_type: Union[str, "PhoneNumberType"],
        capabilities: "PhoneNumberCapabilities",
        assignment_type: Union[str, "PhoneNumberAssignmentType"],
        cost: "PhoneNumberCost",
        purchase_date: Optional[datetime.datetime] = None,
        callback_uri: Optional[str] = None,
        application_id: Optional[str] = None,
        **kwargs
    ):
        super(AcquiredPhoneNumber, self).__init__(**kwargs)
        self.id = id
        self.phone_number = phone_number
        self.country_code = country_code
        self.phone_number_type = phone_number_type
        self.capabilities = capabilities
        self.assignment_type = assignment_type
        self.purchase_date = purchase_date
        self.callback_uri = callback_uri
        self.application_id = application_id
        self.cost = cost


class AcquiredPhoneNumbers(msrest.serialization.Model):
    """The list of acquired phone numbers.

    All required parameters must be populated in order to send to Azure.

    :param phone_numbers: Required. Represents a list of phone numbers.
    :type phone_numbers: list[~azure.communication.administration.models.AcquiredPhoneNumber]
    :param next_link: Represents the URL link to the next page of phone number results.
    :type next_link: str
    """

    _validation = {
        'phone_numbers': {'required': True},
    }

    _attribute_map = {
        'phone_numbers': {'key': 'phoneNumbers', 'type': '[AcquiredPhoneNumber]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        phone_numbers: List["AcquiredPhoneNumber"],
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(AcquiredPhoneNumbers, self).__init__(**kwargs)
        self.phone_numbers = phone_numbers
        self.next_link = next_link


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code.
    :type code: str
    :param message: Required. The error message.
    :type message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.administration.models.CommunicationError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.administration.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innererror', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        code: str,
        message: str,
        **kwargs
    ):
        super(CommunicationError, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = None
        self.details = None
        self.inner_error = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. The Communication Services error.
    :type error: ~azure.communication.administration.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        *,
        error: "CommunicationError",
        **kwargs
    ):
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = error


class PhoneNumberCapabilities(msrest.serialization.Model):
    """Capabilities of a phone number.

    All required parameters must be populated in order to send to Azure.

    :param calling: Required. Capability value for calling. Possible values include: "none",
     "inbound", "outbound", "inbound+outbound".
    :type calling: str or ~azure.communication.administration.models.PhoneNumberCapabilityValue
    :param sms: Required. Capability value for SMS. Possible values include: "none", "inbound",
     "outbound", "inbound+outbound".
    :type sms: str or ~azure.communication.administration.models.PhoneNumberCapabilityValue
    """

    _validation = {
        'calling': {'required': True},
        'sms': {'required': True},
    }

    _attribute_map = {
        'calling': {'key': 'calling', 'type': 'str'},
        'sms': {'key': 'sms', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        calling: Union[str, "PhoneNumberCapabilityValue"],
        sms: Union[str, "PhoneNumberCapabilityValue"],
        **kwargs
    ):
        super(PhoneNumberCapabilities, self).__init__(**kwargs)
        self.calling = calling
        self.sms = sms


class PhoneNumberCapabilitiesRequest(msrest.serialization.Model):
    """Capabilities of a phone number.

    :param calling: Capability value for calling. Possible values include: "none", "inbound",
     "outbound", "inbound+outbound".
    :type calling: str or ~azure.communication.administration.models.PhoneNumberCapabilityValue
    :param sms: Capability value for SMS. Possible values include: "none", "inbound", "outbound",
     "inbound+outbound".
    :type sms: str or ~azure.communication.administration.models.PhoneNumberCapabilityValue
    """

    _attribute_map = {
        'calling': {'key': 'calling', 'type': 'str'},
        'sms': {'key': 'sms', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        calling: Optional[Union[str, "PhoneNumberCapabilityValue"]] = None,
        sms: Optional[Union[str, "PhoneNumberCapabilityValue"]] = None,
        **kwargs
    ):
        super(PhoneNumberCapabilitiesRequest, self).__init__(**kwargs)
        self.calling = calling
        self.sms = sms


class PhoneNumberCost(msrest.serialization.Model):
    """The incurred cost for a single phone number.

    All required parameters must be populated in order to send to Azure.

    :param amount: Required. The cost amount.
    :type amount: float
    :param currency_code: Required. The ISO 4217 currency code for the cost amount, e.g. USD.
    :type currency_code: str
    :param billing_frequency: Required. The frequency with which the cost gets billed. Possible
     values include: "monthly".
    :type billing_frequency: str or ~azure.communication.administration.models.BillingFrequency
    """

    _validation = {
        'amount': {'required': True},
        'currency_code': {'required': True},
        'billing_frequency': {'required': True},
    }

    _attribute_map = {
        'amount': {'key': 'amount', 'type': 'float'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'billing_frequency': {'key': 'billingFrequency', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        amount: float,
        currency_code: str,
        billing_frequency: Union[str, "BillingFrequency"],
        **kwargs
    ):
        super(PhoneNumberCost, self).__init__(**kwargs)
        self.amount = amount
        self.currency_code = currency_code
        self.billing_frequency = billing_frequency


class PhoneNumberOperation(msrest.serialization.Model):
    """Long running operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param status: Required. Status of operation. Possible values include: "notStarted", "running",
     "succeeded", "failed".
    :type status: str or ~azure.communication.administration.models.PhoneNumberOperationStatus
    :param resource_location: URL for retrieving the result of the operation, if any.
    :type resource_location: str
    :param created_date_time: Required. The date that the operation was created.
    :type created_date_time: ~datetime.datetime
    :param error: The Communication Services error.
    :type error: ~azure.communication.administration.models.CommunicationError
    :param id: Required. Id of operation.
    :type id: str
    :param operation_type: Required. The type of operation, e.g. Search. Possible values include:
     "purchase", "releasePhoneNumber", "search", "updatePhoneNumberCapabilities".
    :type operation_type: str or
     ~azure.communication.administration.models.PhoneNumberOperationType
    :ivar last_action_date_time: The most recent date that the operation was changed.
    :vartype last_action_date_time: ~datetime.datetime
    """

    _validation = {
        'status': {'required': True},
        'created_date_time': {'required': True},
        'id': {'required': True},
        'operation_type': {'required': True},
        'last_action_date_time': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'resource_location': {'key': 'resourceLocation', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'CommunicationError'},
        'id': {'key': 'id', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'last_action_date_time': {'key': 'lastActionDateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        status: Union[str, "PhoneNumberOperationStatus"],
        created_date_time: datetime.datetime,
        id: str,
        operation_type: Union[str, "PhoneNumberOperationType"],
        resource_location: Optional[str] = None,
        error: Optional["CommunicationError"] = None,
        **kwargs
    ):
        super(PhoneNumberOperation, self).__init__(**kwargs)
        self.status = status
        self.resource_location = resource_location
        self.created_date_time = created_date_time
        self.error = error
        self.id = id
        self.operation_type = operation_type
        self.last_action_date_time = None


class PhoneNumberPurchaseRequest(msrest.serialization.Model):
    """The phone number search purchase request.

    :param search_id: The search id.
    :type search_id: str
    """

    _attribute_map = {
        'search_id': {'key': 'searchId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        search_id: Optional[str] = None,
        **kwargs
    ):
        super(PhoneNumberPurchaseRequest, self).__init__(**kwargs)
        self.search_id = search_id


class PhoneNumberSearchRequest(msrest.serialization.Model):
    """Represents a phone number search request to find phone numbers. Found phone numbers are temporarily held for a following purchase.

    All required parameters must be populated in order to send to Azure.

    :param phone_number_type: Required. The type of phone numbers to search for, e.g. geographic,
     or tollFree. Possible values include: "geographic", "tollFree".
    :type phone_number_type: str or ~azure.communication.administration.models.PhoneNumberType
    :param assignment_type: Required. The assignment type of the phone numbers to search for. A
     phone number can be assigned to a person, or to an application. Possible values include:
     "user", "application".
    :type assignment_type: str or
     ~azure.communication.administration.models.PhoneNumberAssignmentType
    :param capabilities: Required. Capabilities of a phone number.
    :type capabilities: ~azure.communication.administration.models.PhoneNumberCapabilities
    :param area_code: The area code of the desired phone number, e.g. 425.
    :type area_code: str
    :param quantity: The quantity of phone numbers in the search. Should be at least 1.
    :type quantity: int
    """

    _validation = {
        'phone_number_type': {'required': True},
        'assignment_type': {'required': True},
        'capabilities': {'required': True},
        'quantity': {'maximum': 2147483647, 'minimum': 1},
    }

    _attribute_map = {
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'area_code': {'key': 'areaCode', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        phone_number_type: Union[str, "PhoneNumberType"],
        assignment_type: Union[str, "PhoneNumberAssignmentType"],
        capabilities: "PhoneNumberCapabilities",
        area_code: Optional[str] = None,
        quantity: Optional[int] = None,
        **kwargs
    ):
        super(PhoneNumberSearchRequest, self).__init__(**kwargs)
        self.phone_number_type = phone_number_type
        self.assignment_type = assignment_type
        self.capabilities = capabilities
        self.area_code = area_code
        self.quantity = quantity


class PhoneNumberSearchResult(msrest.serialization.Model):
    """The result of a phone number search operation.

    All required parameters must be populated in order to send to Azure.

    :param search_id: Required. The search id.
    :type search_id: str
    :param phone_numbers: Required. The phone numbers that are available. Can be fewer than the
     desired search quantity.
    :type phone_numbers: list[str]
    :param phone_number_type: Required. The phone number's type, e.g. geographic, or tollFree.
     Possible values include: "geographic", "tollFree".
    :type phone_number_type: str or ~azure.communication.administration.models.PhoneNumberType
    :param assignment_type: Required. Phone number's assignment type. Possible values include:
     "user", "application".
    :type assignment_type: str or
     ~azure.communication.administration.models.PhoneNumberAssignmentType
    :param capabilities: Required. Capabilities of a phone number.
    :type capabilities: ~azure.communication.administration.models.PhoneNumberCapabilities
    :param cost: The incurred cost for a single phone number.
    :type cost: ~azure.communication.administration.models.PhoneNumberCost
    :param search_expires_by: Required. The date that this search result expires and phone numbers
     are no longer on hold. A search result expires in less than 15min, e.g.
     2020-11-19T16:31:49.048Z.
    :type search_expires_by: ~datetime.datetime
    """

    _validation = {
        'search_id': {'required': True},
        'phone_numbers': {'required': True},
        'phone_number_type': {'required': True},
        'assignment_type': {'required': True},
        'capabilities': {'required': True},
        'search_expires_by': {'required': True},
    }

    _attribute_map = {
        'search_id': {'key': 'searchId', 'type': 'str'},
        'phone_numbers': {'key': 'phoneNumbers', 'type': '[str]'},
        'phone_number_type': {'key': 'phoneNumberType', 'type': 'str'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': 'PhoneNumberCapabilities'},
        'cost': {'key': 'cost', 'type': 'PhoneNumberCost'},
        'search_expires_by': {'key': 'searchExpiresBy', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        search_id: str,
        phone_numbers: List[str],
        phone_number_type: Union[str, "PhoneNumberType"],
        assignment_type: Union[str, "PhoneNumberAssignmentType"],
        capabilities: "PhoneNumberCapabilities",
        search_expires_by: datetime.datetime,
        cost: Optional["PhoneNumberCost"] = None,
        **kwargs
    ):
        super(PhoneNumberSearchResult, self).__init__(**kwargs)
        self.search_id = search_id
        self.phone_numbers = phone_numbers
        self.phone_number_type = phone_number_type
        self.assignment_type = assignment_type
        self.capabilities = capabilities
        self.cost = cost
        self.search_expires_by = search_expires_by


class PhoneNumberUpdateRequest(msrest.serialization.Model):
    """Property updates for a phone number.

    :param callback_uri: The webhook for receiving incoming events.
     e.g. "https://{{site-name}}.azurewebsites.net/api/updates".
     Please read https://docs.microsoft.com/en-us/azure/communication-services/concepts/event-
     handling
     for integration with Azure Event Grid to deliver real-time event notifications.
    :type callback_uri: str
    :param application_id: The application id of the application to which to configure.
    :type application_id: str
    """

    _attribute_map = {
        'callback_uri': {'key': 'callbackUri', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        callback_uri: Optional[str] = None,
        application_id: Optional[str] = None,
        **kwargs
    ):
        super(PhoneNumberUpdateRequest, self).__init__(**kwargs)
        self.callback_uri = callback_uri
        self.application_id = application_id
