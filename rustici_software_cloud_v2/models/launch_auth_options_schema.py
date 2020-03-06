# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LaunchAuthOptionsSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ip_address=None, fingerprint=None, expiry=None, sliding_expiry=None):
        """
        LaunchAuthOptionsSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ip_address': 'bool',
            'fingerprint': 'bool',
            'expiry': 'int',
            'sliding_expiry': 'int'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'fingerprint': 'fingerprint',
            'expiry': 'expiry',
            'sliding_expiry': 'slidingExpiry'
        }

        self._ip_address = ip_address
        self._fingerprint = fingerprint
        self._expiry = expiry
        self._sliding_expiry = sliding_expiry

    @property
    def ip_address(self):
        """
        Gets the ip_address of this LaunchAuthOptionsSchema.

        :return: The ip_address of this LaunchAuthOptionsSchema.
        :rtype: bool
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this LaunchAuthOptionsSchema.

        :param ip_address: The ip_address of this LaunchAuthOptionsSchema.
        :type: bool
        """

        self._ip_address = ip_address

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this LaunchAuthOptionsSchema.

        :return: The fingerprint of this LaunchAuthOptionsSchema.
        :rtype: bool
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this LaunchAuthOptionsSchema.

        :param fingerprint: The fingerprint of this LaunchAuthOptionsSchema.
        :type: bool
        """

        self._fingerprint = fingerprint

    @property
    def expiry(self):
        """
        Gets the expiry of this LaunchAuthOptionsSchema.

        :return: The expiry of this LaunchAuthOptionsSchema.
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """
        Sets the expiry of this LaunchAuthOptionsSchema.

        :param expiry: The expiry of this LaunchAuthOptionsSchema.
        :type: int
        """

        self._expiry = expiry

    @property
    def sliding_expiry(self):
        """
        Gets the sliding_expiry of this LaunchAuthOptionsSchema.

        :return: The sliding_expiry of this LaunchAuthOptionsSchema.
        :rtype: int
        """
        return self._sliding_expiry

    @sliding_expiry.setter
    def sliding_expiry(self, sliding_expiry):
        """
        Sets the sliding_expiry of this LaunchAuthOptionsSchema.

        :param sliding_expiry: The sliding_expiry of this LaunchAuthOptionsSchema.
        :type: int
        """

        self._sliding_expiry = sliding_expiry

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LaunchAuthOptionsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
