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
from rustici_software_cloud_v2.models.paginated_list import PaginatedList  # noqa: F401,E501


class PublicInvitationList(PaginatedList):
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
        'more': 'str',
        'invitations': 'list[PublicInvitationSchema]'
    }

    attribute_map = {
        'more': 'more',
        'invitations': 'invitations'
    }

    def __init__(self, more=None, invitations=None):  # noqa: E501
        """PublicInvitationList - a model defined in Swagger"""  # noqa: E501

        self._invitations = None
        self.discriminator = None

        if invitations is not None:
            self.invitations = invitations

        super().__init__(more)  # noqa: E501

    @property
    def invitations(self):
        """Gets the invitations of this PublicInvitationList.  # noqa: E501

        A list of public invitation objects.  # noqa: E501

        :return: The invitations of this PublicInvitationList.  # noqa: E501
        :rtype: list[PublicInvitationSchema]
        """
        return self._invitations

    @invitations.setter
    def invitations(self, invitations):
        """Sets the invitations of this PublicInvitationList.

        A list of public invitation objects.  # noqa: E501

        :param invitations: The invitations of this PublicInvitationList.  # noqa: E501
        :type: list[PublicInvitationSchema]
        """

        self._invitations = invitations

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
        if issubclass(PublicInvitationList, dict):
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
        if not isinstance(other, PublicInvitationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
