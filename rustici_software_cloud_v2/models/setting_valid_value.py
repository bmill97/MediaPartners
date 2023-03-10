# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SettingValidValue(object):
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
        'value': 'str',
        'value_description': 'str'
    }

    attribute_map = {
        'value': 'value',
        'value_description': 'valueDescription'
    }

    def __init__(self, value=None, value_description=None):  # noqa: E501
        """SettingValidValue - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._value_description = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if value_description is not None:
            self.value_description = value_description

    @property
    def value(self):
        """Gets the value of this SettingValidValue.  # noqa: E501

        :return: The value of this SettingValidValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SettingValidValue.

        :param value: The value of this SettingValidValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_description(self):
        """Gets the value_description of this SettingValidValue.  # noqa: E501

        Description of what this valid value means, how it will be applied if used in a setting  # noqa: E501

        :return: The value_description of this SettingValidValue.  # noqa: E501
        :rtype: str
        """
        return self._value_description

    @value_description.setter
    def value_description(self, value_description):
        """Sets the value_description of this SettingValidValue.

        Description of what this valid value means, how it will be applied if used in a setting  # noqa: E501

        :param value_description: The value_description of this SettingValidValue.  # noqa: E501
        :type: str
        """

        self._value_description = value_description

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
        if issubclass(SettingValidValue, dict):
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
        if not isinstance(other, SettingValidValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
