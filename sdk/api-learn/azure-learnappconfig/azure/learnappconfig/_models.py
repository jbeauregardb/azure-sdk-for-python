from enum import Enum
class ConfigurationSetting(object):
    """A configuration value.

    :param str key: The key name of the setting.
    :param str value: The value of the setting.
    :keyword str label: The setting label.
    :ivar str etag: Entity tag (etag) of the setting.
    :ivar  ~datetime.datetime last_modified: The time the setting was last modified.
    :ivar bool read_only: Whether the setting is read-only.
    :ivar str content_type: The content type of the setting value.
    :ivar dict[str, str] tags: User tags added to the setting.
    """

    def __init__(self, key, value, **kwargs):
        # type: (str, str, Any) -> None
        self.key = key
        self.value = value
        self.etag = kwargs.get('etag', None)
        self.label = kwargs.get('label', None)
        self.content_type = kwargs.get('content_type', None)
        self.last_modified = kwargs.get('last_modified', None)
        self.read_only = kwargs.get('read_only', None)
        self.tags = kwargs.get('tags', None)
    
    def __repr__(self):
        # type: () -> str
        pass
    
    def __getitem__(self, *args):
        # type: (Any) -> Any
        pass
    
    def __contains__(self, *args):
        # type: (Any) -> Any
        pass

class SettingFields(str, Enum):
    """The specific settings for a given ConfigurationSetting that can be selected."""

    KEY = "key"
    LABEL = "label"
    CONTENT_TYPE = "content_type"
    VALUE = "value"
    LAST_MODIFIED = "last_modified"
    TAGS = "tags"
    READ_ONLY = "locked"
    ETAG = "etag"