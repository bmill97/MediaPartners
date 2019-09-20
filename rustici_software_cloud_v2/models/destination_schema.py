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


class DestinationSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, tags=None, email=None, notes=None):
        """
        DestinationSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'tags': 'list[str]',
            'email': 'str',
            'notes': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'tags': 'tags',
            'email': 'email',
            'notes': 'notes'
        }

        self._name = name
        self._tags = tags
        self._email = email
        self._notes = notes

    @property
    def name(self):
        """
        Gets the name of this DestinationSchema.
        The destination's name.

        :return: The name of this DestinationSchema.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DestinationSchema.
        The destination's name.

        :param name: The name of this DestinationSchema.
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """
        Gets the tags of this DestinationSchema.
        Optional array of tags.

        :return: The tags of this DestinationSchema.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this DestinationSchema.
        Optional array of tags.

        :param tags: The tags of this DestinationSchema.
        :type: list[str]
        """

        self._tags = tags

    @property
    def email(self):
        """
        Gets the email of this DestinationSchema.
        SCORM Cloud user e-mail associated with this destination. If this is not provided, it will default to the owner of the Realm. 

        :return: The email of this DestinationSchema.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this DestinationSchema.
        SCORM Cloud user e-mail associated with this destination. If this is not provided, it will default to the owner of the Realm. 

        :param email: The email of this DestinationSchema.
        :type: str
        """

        self._email = email

    @property
    def notes(self):
        """
        Gets the notes of this DestinationSchema.
        Any provided notes about this Destination

        :return: The notes of this DestinationSchema.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this DestinationSchema.
        Any provided notes about this Destination

        :param notes: The notes of this DestinationSchema.
        :type: str
        """

        self._notes = notes

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
        if not isinstance(other, DestinationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
