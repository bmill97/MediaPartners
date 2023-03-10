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


class XapiStatementPipeListSchema(object):
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
        'xapi_statement_pipes': 'list[XapiStatementPipeSchema]'
    }

    attribute_map = {
        'xapi_statement_pipes': 'xapiStatementPipes'
    }

    def __init__(self, xapi_statement_pipes=None):  # noqa: E501
        """XapiStatementPipeListSchema - a model defined in Swagger"""  # noqa: E501

        self._xapi_statement_pipes = None
        self.discriminator = None

        self.xapi_statement_pipes = xapi_statement_pipes

    @property
    def xapi_statement_pipes(self):
        """Gets the xapi_statement_pipes of this XapiStatementPipeListSchema.  # noqa: E501

        :return: The xapi_statement_pipes of this XapiStatementPipeListSchema.  # noqa: E501
        :rtype: list[XapiStatementPipeSchema]
        """
        return self._xapi_statement_pipes

    @xapi_statement_pipes.setter
    def xapi_statement_pipes(self, xapi_statement_pipes):
        """Sets the xapi_statement_pipes of this XapiStatementPipeListSchema.

        :param xapi_statement_pipes: The xapi_statement_pipes of this XapiStatementPipeListSchema.  # noqa: E501
        :type: list[XapiStatementPipeSchema]
        """
        if xapi_statement_pipes is None:
            raise ValueError("Invalid value for `xapi_statement_pipes`, must not be `None`")  # noqa: E501

        self._xapi_statement_pipes = xapi_statement_pipes

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
        if issubclass(XapiStatementPipeListSchema, dict):
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
        if not isinstance(other, XapiStatementPipeListSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
