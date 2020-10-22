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


class ConnectorContentListEntrySchema(object):
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
        'connector_type': 'str',
        'connector_id': 'str',
        'details': 'ConnectorContentItemSchema'
    }

    attribute_map = {
        'connector_type': 'connectorType',
        'connector_id': 'connectorId',
        'details': 'details'
    }

    def __init__(self, connector_type=None, connector_id=None, details=None):  # noqa: E501
        """ConnectorContentListEntrySchema - a model defined in Swagger"""  # noqa: E501

        self._connector_type = None
        self._connector_id = None
        self._details = None
        self.discriminator = None

        if connector_type is not None:
            self.connector_type = connector_type
        if connector_id is not None:
            self.connector_id = connector_id
        if details is not None:
            self.details = details

    @property
    def connector_type(self):
        """Gets the connector_type of this ConnectorContentListEntrySchema.  # noqa: E501


        :return: The connector_type of this ConnectorContentListEntrySchema.  # noqa: E501
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """Sets the connector_type of this ConnectorContentListEntrySchema.


        :param connector_type: The connector_type of this ConnectorContentListEntrySchema.  # noqa: E501
        :type: str
        """

        self._connector_type = connector_type

    @property
    def connector_id(self):
        """Gets the connector_id of this ConnectorContentListEntrySchema.  # noqa: E501


        :return: The connector_id of this ConnectorContentListEntrySchema.  # noqa: E501
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ConnectorContentListEntrySchema.


        :param connector_id: The connector_id of this ConnectorContentListEntrySchema.  # noqa: E501
        :type: str
        """

        self._connector_id = connector_id

    @property
    def details(self):
        """Gets the details of this ConnectorContentListEntrySchema.  # noqa: E501


        :return: The details of this ConnectorContentListEntrySchema.  # noqa: E501
        :rtype: ConnectorContentItemSchema
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ConnectorContentListEntrySchema.


        :param details: The details of this ConnectorContentListEntrySchema.  # noqa: E501
        :type: ConnectorContentItemSchema
        """

        self._details = details

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
        if issubclass(ConnectorContentListEntrySchema, dict):
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
        if not isinstance(other, ConnectorContentListEntrySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other