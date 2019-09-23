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


class XapiScore(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, scaled=None, raw=None, min=None, max=None):
        """
        XapiScore - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'scaled': 'float',
            'raw': 'float',
            'min': 'float',
            'max': 'float'
        }

        self.attribute_map = {
            'scaled': 'scaled',
            'raw': 'raw',
            'min': 'min',
            'max': 'max'
        }

        self._scaled = scaled
        self._raw = raw
        self._min = min
        self._max = max

    @property
    def scaled(self):
        """
        Gets the scaled of this XapiScore.

        :return: The scaled of this XapiScore.
        :rtype: float
        """
        return self._scaled

    @scaled.setter
    def scaled(self, scaled):
        """
        Sets the scaled of this XapiScore.

        :param scaled: The scaled of this XapiScore.
        :type: float
        """

        self._scaled = scaled

    @property
    def raw(self):
        """
        Gets the raw of this XapiScore.

        :return: The raw of this XapiScore.
        :rtype: float
        """
        return self._raw

    @raw.setter
    def raw(self, raw):
        """
        Sets the raw of this XapiScore.

        :param raw: The raw of this XapiScore.
        :type: float
        """

        self._raw = raw

    @property
    def min(self):
        """
        Gets the min of this XapiScore.

        :return: The min of this XapiScore.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this XapiScore.

        :param min: The min of this XapiScore.
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """
        Gets the max of this XapiScore.

        :return: The max of this XapiScore.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this XapiScore.

        :param max: The max of this XapiScore.
        :type: float
        """

        self._max = max

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
        if not isinstance(other, XapiScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
