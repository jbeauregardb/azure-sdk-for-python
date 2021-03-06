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


class ApplicationArtifactType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The managed application artifact type.
    """

    TEMPLATE = "Template"
    CUSTOM = "Custom"

class ApplicationLockLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The managed application lock level.
    """

    CAN_NOT_DELETE = "CanNotDelete"
    READ_ONLY = "ReadOnly"
    NONE = "None"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Provisioning status of the managed application.
    """

    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
