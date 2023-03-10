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


class ZoomiCourseOptionsSchema(object):
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
        'nti': 'str',
        'cta': 'str'
    }

    attribute_map = {
        'nti': 'nti',
        'cta': 'cta'
    }

    def __init__(self, nti=None, cta=None):  # noqa: E501
        """ZoomiCourseOptionsSchema - a model defined in Swagger"""  # noqa: E501

        self._nti = None
        self._cta = None
        self.discriminator = None

        self.nti = nti
        self.cta = cta

    @property
    def nti(self):
        """Gets the nti of this ZoomiCourseOptionsSchema.  # noqa: E501

        :return: The nti of this ZoomiCourseOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._nti

    @nti.setter
    def nti(self, nti):
        """Sets the nti of this ZoomiCourseOptionsSchema.

        :param nti: The nti of this ZoomiCourseOptionsSchema.  # noqa: E501
        :type: str
        """
        if nti is None:
            raise ValueError("Invalid value for `nti`, must not be `None`")  # noqa: E501

        self._nti = nti

    @property
    def cta(self):
        """Gets the cta of this ZoomiCourseOptionsSchema.  # noqa: E501

        :return: The cta of this ZoomiCourseOptionsSchema.  # noqa: E501
        :rtype: str
        """
        return self._cta

    @cta.setter
    def cta(self, cta):
        """Sets the cta of this ZoomiCourseOptionsSchema.

        :param cta: The cta of this ZoomiCourseOptionsSchema.  # noqa: E501
        :type: str
        """
        if cta is None:
            raise ValueError("Invalid value for `cta`, must not be `None`")  # noqa: E501

        self._cta = cta

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
        if issubclass(ZoomiCourseOptionsSchema, dict):
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
        if not isinstance(other, ZoomiCourseOptionsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
