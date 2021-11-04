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


class TokenRequestSchema(object):
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
        'permissions': 'PermissionsSchema',
        'expiry': 'datetime'
    }

    attribute_map = {
        'permissions': 'permissions',
        'expiry': 'expiry'
    }

    def __init__(self, permissions=None, expiry=None):  # noqa: E501
        """TokenRequestSchema - a model defined in Swagger"""  # noqa: E501

        self._permissions = None
        self._expiry = None
        self.discriminator = None

        self.permissions = permissions
        self.expiry = expiry

    @property
    def permissions(self):
        """Gets the permissions of this TokenRequestSchema.  # noqa: E501

        :return: The permissions of this TokenRequestSchema.  # noqa: E501
        :rtype: PermissionsSchema
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this TokenRequestSchema.

        :param permissions: The permissions of this TokenRequestSchema.  # noqa: E501
        :type: PermissionsSchema
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def expiry(self):
        """Gets the expiry of this TokenRequestSchema.  # noqa: E501

        Expiration of the token. This should not be set far in the future, as there is no way to invalidate an individual token.  # noqa: E501

        :return: The expiry of this TokenRequestSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this TokenRequestSchema.

        Expiration of the token. This should not be set far in the future, as there is no way to invalidate an individual token.  # noqa: E501

        :param expiry: The expiry of this TokenRequestSchema.  # noqa: E501
        :type: datetime
        """
        if expiry is None:
            raise ValueError("Invalid value for `expiry`, must not be `None`")  # noqa: E501

        self._expiry = expiry

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
        if issubclass(TokenRequestSchema, dict):
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
        if not isinstance(other, TokenRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
