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


class Lti13ToolConfigurationSchema(object):
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
        'public_key': 'str',
        'oidc_login_initiations_url': 'str',
        'redirect_uri': 'str',
        'json_web_key_set_url': 'str'
    }

    attribute_map = {
        'public_key': 'publicKey',
        'oidc_login_initiations_url': 'oidcLoginInitiationsUrl',
        'redirect_uri': 'redirectUri',
        'json_web_key_set_url': 'jsonWebKeySetUrl'
    }

    def __init__(self, public_key=None, oidc_login_initiations_url=None, redirect_uri=None, json_web_key_set_url=None):  # noqa: E501
        """Lti13ToolConfigurationSchema - a model defined in Swagger"""  # noqa: E501

        self._public_key = None
        self._oidc_login_initiations_url = None
        self._redirect_uri = None
        self._json_web_key_set_url = None
        self.discriminator = None

        self.public_key = public_key
        self.oidc_login_initiations_url = oidc_login_initiations_url
        self.redirect_uri = redirect_uri
        self.json_web_key_set_url = json_web_key_set_url

    @property
    def public_key(self):
        """Gets the public_key of this Lti13ToolConfigurationSchema.  # noqa: E501

        Public key for LTI 1.3 tool  # noqa: E501

        :return: The public_key of this Lti13ToolConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Lti13ToolConfigurationSchema.

        Public key for LTI 1.3 tool  # noqa: E501

        :param public_key: The public_key of this Lti13ToolConfigurationSchema.  # noqa: E501
        :type: str
        """
        if public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def oidc_login_initiations_url(self):
        """Gets the oidc_login_initiations_url of this Lti13ToolConfigurationSchema.  # noqa: E501

        Endpoint where the OIDC Authorization flow will be initiated  # noqa: E501

        :return: The oidc_login_initiations_url of this Lti13ToolConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._oidc_login_initiations_url

    @oidc_login_initiations_url.setter
    def oidc_login_initiations_url(self, oidc_login_initiations_url):
        """Sets the oidc_login_initiations_url of this Lti13ToolConfigurationSchema.

        Endpoint where the OIDC Authorization flow will be initiated  # noqa: E501

        :param oidc_login_initiations_url: The oidc_login_initiations_url of this Lti13ToolConfigurationSchema.  # noqa: E501
        :type: str
        """
        if oidc_login_initiations_url is None:
            raise ValueError("Invalid value for `oidc_login_initiations_url`, must not be `None`")  # noqa: E501

        self._oidc_login_initiations_url = oidc_login_initiations_url

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this Lti13ToolConfigurationSchema.  # noqa: E501

        Endpoint where the OIDC Authorization Response should be sent  # noqa: E501

        :return: The redirect_uri of this Lti13ToolConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this Lti13ToolConfigurationSchema.

        Endpoint where the OIDC Authorization Response should be sent  # noqa: E501

        :param redirect_uri: The redirect_uri of this Lti13ToolConfigurationSchema.  # noqa: E501
        :type: str
        """
        if redirect_uri is None:
            raise ValueError("Invalid value for `redirect_uri`, must not be `None`")  # noqa: E501

        self._redirect_uri = redirect_uri

    @property
    def json_web_key_set_url(self):
        """Gets the json_web_key_set_url of this Lti13ToolConfigurationSchema.  # noqa: E501

        Path to the tool's JSON Web Key Set  # noqa: E501

        :return: The json_web_key_set_url of this Lti13ToolConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._json_web_key_set_url

    @json_web_key_set_url.setter
    def json_web_key_set_url(self, json_web_key_set_url):
        """Sets the json_web_key_set_url of this Lti13ToolConfigurationSchema.

        Path to the tool's JSON Web Key Set  # noqa: E501

        :param json_web_key_set_url: The json_web_key_set_url of this Lti13ToolConfigurationSchema.  # noqa: E501
        :type: str
        """
        if json_web_key_set_url is None:
            raise ValueError("Invalid value for `json_web_key_set_url`, must not be `None`")  # noqa: E501

        self._json_web_key_set_url = json_web_key_set_url

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
        if issubclass(Lti13ToolConfigurationSchema, dict):
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
        if not isinstance(other, Lti13ToolConfigurationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
