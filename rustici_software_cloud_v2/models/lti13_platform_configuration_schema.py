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


class Lti13PlatformConfigurationSchema(object):
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
        'client_id': 'str',
        'platform_issuer_identifier': 'str',
        'deployment_id': 'str',
        'oidc_authorization_endpoint': 'str',
        'json_web_key_set_url': 'str',
        'access_token_url': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'platform_issuer_identifier': 'platformIssuerIdentifier',
        'deployment_id': 'deploymentId',
        'oidc_authorization_endpoint': 'oidcAuthorizationEndpoint',
        'json_web_key_set_url': 'jsonWebKeySetUrl',
        'access_token_url': 'accessTokenUrl'
    }

    def __init__(self, client_id=None, platform_issuer_identifier=None, deployment_id=None, oidc_authorization_endpoint=None, json_web_key_set_url=None, access_token_url=None):  # noqa: E501
        """Lti13PlatformConfigurationSchema - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._platform_issuer_identifier = None
        self._deployment_id = None
        self._oidc_authorization_endpoint = None
        self._json_web_key_set_url = None
        self._access_token_url = None
        self.discriminator = None

        self.client_id = client_id
        self.platform_issuer_identifier = platform_issuer_identifier
        self.deployment_id = deployment_id
        self.oidc_authorization_endpoint = oidc_authorization_endpoint
        self.json_web_key_set_url = json_web_key_set_url
        if access_token_url is not None:
            self.access_token_url = access_token_url

    @property
    def client_id(self):
        """Gets the client_id of this Lti13PlatformConfigurationSchema.  # noqa: E501

        OAuth2 client Id for this tool  # noqa: E501

        :return: The client_id of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this Lti13PlatformConfigurationSchema.

        OAuth2 client Id for this tool  # noqa: E501

        :param client_id: The client_id of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def platform_issuer_identifier(self):
        """Gets the platform_issuer_identifier of this Lti13PlatformConfigurationSchema.  # noqa: E501

        Issuer identifier identifying the learning platform  # noqa: E501

        :return: The platform_issuer_identifier of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._platform_issuer_identifier

    @platform_issuer_identifier.setter
    def platform_issuer_identifier(self, platform_issuer_identifier):
        """Sets the platform_issuer_identifier of this Lti13PlatformConfigurationSchema.

        Issuer identifier identifying the learning platform  # noqa: E501

        :param platform_issuer_identifier: The platform_issuer_identifier of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """
        if platform_issuer_identifier is None:
            raise ValueError("Invalid value for `platform_issuer_identifier`, must not be `None`")  # noqa: E501

        self._platform_issuer_identifier = platform_issuer_identifier

    @property
    def deployment_id(self):
        """Gets the deployment_id of this Lti13PlatformConfigurationSchema.  # noqa: E501

        An unchanging identifier (locally unique within the platformIssuerIdentifier) for the platform-tool integration  # noqa: E501

        :return: The deployment_id of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this Lti13PlatformConfigurationSchema.

        An unchanging identifier (locally unique within the platformIssuerIdentifier) for the platform-tool integration  # noqa: E501

        :param deployment_id: The deployment_id of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """
        if deployment_id is None:
            raise ValueError("Invalid value for `deployment_id`, must not be `None`")  # noqa: E501

        self._deployment_id = deployment_id

    @property
    def oidc_authorization_endpoint(self):
        """Gets the oidc_authorization_endpoint of this Lti13PlatformConfigurationSchema.  # noqa: E501

        Endpoint that will initiate the OIDC Authentication Request  # noqa: E501

        :return: The oidc_authorization_endpoint of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._oidc_authorization_endpoint

    @oidc_authorization_endpoint.setter
    def oidc_authorization_endpoint(self, oidc_authorization_endpoint):
        """Sets the oidc_authorization_endpoint of this Lti13PlatformConfigurationSchema.

        Endpoint that will initiate the OIDC Authentication Request  # noqa: E501

        :param oidc_authorization_endpoint: The oidc_authorization_endpoint of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """
        if oidc_authorization_endpoint is None:
            raise ValueError("Invalid value for `oidc_authorization_endpoint`, must not be `None`")  # noqa: E501

        self._oidc_authorization_endpoint = oidc_authorization_endpoint

    @property
    def json_web_key_set_url(self):
        """Gets the json_web_key_set_url of this Lti13PlatformConfigurationSchema.  # noqa: E501

        Path to the platform's JSON Web Key Set  # noqa: E501

        :return: The json_web_key_set_url of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._json_web_key_set_url

    @json_web_key_set_url.setter
    def json_web_key_set_url(self, json_web_key_set_url):
        """Sets the json_web_key_set_url of this Lti13PlatformConfigurationSchema.

        Path to the platform's JSON Web Key Set  # noqa: E501

        :param json_web_key_set_url: The json_web_key_set_url of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """
        if json_web_key_set_url is None:
            raise ValueError("Invalid value for `json_web_key_set_url`, must not be `None`")  # noqa: E501

        self._json_web_key_set_url = json_web_key_set_url

    @property
    def access_token_url(self):
        """Gets the access_token_url of this Lti13PlatformConfigurationSchema.  # noqa: E501

        Endpoint that will return OAuth 2 access tokens for the platform  # noqa: E501

        :return: The access_token_url of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :rtype: str
        """
        return self._access_token_url

    @access_token_url.setter
    def access_token_url(self, access_token_url):
        """Sets the access_token_url of this Lti13PlatformConfigurationSchema.

        Endpoint that will return OAuth 2 access tokens for the platform  # noqa: E501

        :param access_token_url: The access_token_url of this Lti13PlatformConfigurationSchema.  # noqa: E501
        :type: str
        """

        self._access_token_url = access_token_url

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
        if issubclass(Lti13PlatformConfigurationSchema, dict):
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
        if not isinstance(other, Lti13PlatformConfigurationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
