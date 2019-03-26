# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0 beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rustici_software_cloud_v2.models.setting_valid_value import SettingValidValue  # noqa: F401,E501


class SettingMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default': 'str',
        'data_type': 'str',
        'setting_description': 'str',
        'level': 'str',
        'learning_standards': 'list[str]',
        'learning_standard_variant': 'str',
        'fallback': 'str',
        'valid_values': 'list[SettingValidValue]'
    }

    attribute_map = {
        'default': 'default',
        'data_type': 'dataType',
        'setting_description': 'settingDescription',
        'level': 'level',
        'learning_standards': 'learningStandards',
        'learning_standard_variant': 'learningStandardVariant',
        'fallback': 'fallback',
        'valid_values': 'validValues'
    }

    def __init__(self, default=None, data_type=None, setting_description=None, level=None, learning_standards=None, learning_standard_variant='either', fallback=None, valid_values=None):  # noqa: E501
        """SettingMetadata - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._data_type = None
        self._setting_description = None
        self._level = None
        self._learning_standards = None
        self._learning_standard_variant = None
        self._fallback = None
        self._valid_values = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if data_type is not None:
            self.data_type = data_type
        if setting_description is not None:
            self.setting_description = setting_description
        if level is not None:
            self.level = level
        if learning_standards is not None:
            self.learning_standards = learning_standards
        if learning_standard_variant is not None:
            self.learning_standard_variant = learning_standard_variant
        if fallback is not None:
            self.fallback = fallback
        if valid_values is not None:
            self.valid_values = valid_values

    @property
    def default(self):
        """Gets the default of this SettingMetadata.  # noqa: E501

        Default value of this setting  # noqa: E501

        :return: The default of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this SettingMetadata.

        Default value of this setting  # noqa: E501

        :param default: The default of this SettingMetadata.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def data_type(self):
        """Gets the data_type of this SettingMetadata.  # noqa: E501

        The data type of this setting  # noqa: E501

        :return: The data_type of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this SettingMetadata.

        The data type of this setting  # noqa: E501

        :param data_type: The data_type of this SettingMetadata.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def setting_description(self):
        """Gets the setting_description of this SettingMetadata.  # noqa: E501

        description of this setting  # noqa: E501

        :return: The setting_description of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._setting_description

    @setting_description.setter
    def setting_description(self, setting_description):
        """Sets the setting_description of this SettingMetadata.

        description of this setting  # noqa: E501

        :param setting_description: The setting_description of this SettingMetadata.  # noqa: E501
        :type: str
        """

        self._setting_description = setting_description

    @property
    def level(self):
        """Gets the level of this SettingMetadata.  # noqa: E501

        The level this setting will be applied at, which limits where it can be set. For example, WebPathToContentRoot is applied at the application level, so it's not valid to set it for a registration.  # noqa: E501

        :return: The level of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SettingMetadata.

        The level this setting will be applied at, which limits where it can be set. For example, WebPathToContentRoot is applied at the application level, so it's not valid to set it for a registration.  # noqa: E501

        :param level: The level of this SettingMetadata.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def learning_standards(self):
        """Gets the learning_standards of this SettingMetadata.  # noqa: E501

        The list of learning standards this setting applies to. If not present, this setting is not limited to certain learning standards.  # noqa: E501

        :return: The learning_standards of this SettingMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._learning_standards

    @learning_standards.setter
    def learning_standards(self, learning_standards):
        """Sets the learning_standards of this SettingMetadata.

        The list of learning standards this setting applies to. If not present, this setting is not limited to certain learning standards.  # noqa: E501

        :param learning_standards: The learning_standards of this SettingMetadata.  # noqa: E501
        :type: list[str]
        """

        self._learning_standards = learning_standards

    @property
    def learning_standard_variant(self):
        """Gets the learning_standard_variant of this SettingMetadata.  # noqa: E501

        Does this setting apply to only single-SCO packages, only multi-SCO, or either?  # noqa: E501

        :return: The learning_standard_variant of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._learning_standard_variant

    @learning_standard_variant.setter
    def learning_standard_variant(self, learning_standard_variant):
        """Sets the learning_standard_variant of this SettingMetadata.

        Does this setting apply to only single-SCO packages, only multi-SCO, or either?  # noqa: E501

        :param learning_standard_variant: The learning_standard_variant of this SettingMetadata.  # noqa: E501
        :type: str
        """
        allowed_values = ["singleScoOnly", "multiScoOnly", "either"]  # noqa: E501
        if learning_standard_variant not in allowed_values:
            raise ValueError(
                "Invalid value for `learning_standard_variant` ({0}), must be one of {1}"  # noqa: E501
                .format(learning_standard_variant, allowed_values)
            )

        self._learning_standard_variant = learning_standard_variant

    @property
    def fallback(self):
        """Gets the fallback of this SettingMetadata.  # noqa: E501

        A setting that will be used instead of this setting if no value is provided for this setting (This is similar to a default, except that the the value of another setting is being used instead of a fixed default value).  # noqa: E501

        :return: The fallback of this SettingMetadata.  # noqa: E501
        :rtype: str
        """
        return self._fallback

    @fallback.setter
    def fallback(self, fallback):
        """Sets the fallback of this SettingMetadata.

        A setting that will be used instead of this setting if no value is provided for this setting (This is similar to a default, except that the the value of another setting is being used instead of a fixed default value).  # noqa: E501

        :param fallback: The fallback of this SettingMetadata.  # noqa: E501
        :type: str
        """

        self._fallback = fallback

    @property
    def valid_values(self):
        """Gets the valid_values of this SettingMetadata.  # noqa: E501

        For settings with a fixed list of valid values, the list of those values  # noqa: E501

        :return: The valid_values of this SettingMetadata.  # noqa: E501
        :rtype: list[SettingValidValue]
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        """Sets the valid_values of this SettingMetadata.

        For settings with a fixed list of valid values, the list of those values  # noqa: E501

        :param valid_values: The valid_values of this SettingMetadata.  # noqa: E501
        :type: list[SettingValidValue]
        """

        self._valid_values = valid_values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SettingMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettingMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other