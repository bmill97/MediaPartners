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


class DispatchLtiInfoSchema(object):
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
        'url': 'str',
        'consumer_key': 'str',
        'shared_secret': 'str'
    }

    attribute_map = {
        'url': 'url',
        'consumer_key': 'consumerKey',
        'shared_secret': 'sharedSecret'
    }

    def __init__(self, url=None, consumer_key=None, shared_secret=None):  # noqa: E501
        """DispatchLtiInfoSchema - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._consumer_key = None
        self._shared_secret = None
        self.discriminator = None

        self.url = url
        self.consumer_key = consumer_key
        self.shared_secret = shared_secret

    @property
    def url(self):
        """Gets the url of this DispatchLtiInfoSchema.  # noqa: E501

        The LTI launch URL for this dispatch  # noqa: E501

        :return: The url of this DispatchLtiInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DispatchLtiInfoSchema.

        The LTI launch URL for this dispatch  # noqa: E501

        :param url: The url of this DispatchLtiInfoSchema.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def consumer_key(self):
        """Gets the consumer_key of this DispatchLtiInfoSchema.  # noqa: E501

        The OAuth consumer key that identifies the tool consumer for this dispatch.  # noqa: E501

        :return: The consumer_key of this DispatchLtiInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """Sets the consumer_key of this DispatchLtiInfoSchema.

        The OAuth consumer key that identifies the tool consumer for this dispatch.  # noqa: E501

        :param consumer_key: The consumer_key of this DispatchLtiInfoSchema.  # noqa: E501
        :type: str
        """
        if consumer_key is None:
            raise ValueError("Invalid value for `consumer_key`, must not be `None`")  # noqa: E501

        self._consumer_key = consumer_key

    @property
    def shared_secret(self):
        """Gets the shared_secret of this DispatchLtiInfoSchema.  # noqa: E501

        The OAuth secret to be used for LTI authentication for this dispatch.  # noqa: E501

        :return: The shared_secret of this DispatchLtiInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._shared_secret

    @shared_secret.setter
    def shared_secret(self, shared_secret):
        """Sets the shared_secret of this DispatchLtiInfoSchema.

        The OAuth secret to be used for LTI authentication for this dispatch.  # noqa: E501

        :param shared_secret: The shared_secret of this DispatchLtiInfoSchema.  # noqa: E501
        :type: str
        """
        if shared_secret is None:
            raise ValueError("Invalid value for `shared_secret`, must not be `None`")  # noqa: E501

        self._shared_secret = shared_secret

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
        if issubclass(DispatchLtiInfoSchema, dict):
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
        if not isinstance(other, DispatchLtiInfoSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
