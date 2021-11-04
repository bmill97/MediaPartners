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


class XapiAgentGroup(object):
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
        'object_type': 'str',
        'name': 'str',
        'mbox': 'str',
        'mbox_sha1sum': 'str',
        'openid': 'str',
        'account': 'XapiAccount',
        'member': 'list[XapiAgentGroup]'
    }

    attribute_map = {
        'object_type': 'objectType',
        'name': 'name',
        'mbox': 'mbox',
        'mbox_sha1sum': 'mbox_sha1sum',
        'openid': 'openid',
        'account': 'account',
        'member': 'member'
    }

    def __init__(self, object_type=None, name=None, mbox=None, mbox_sha1sum=None, openid=None, account=None, member=None):  # noqa: E501
        """XapiAgentGroup - a model defined in Swagger"""  # noqa: E501

        self._object_type = None
        self._name = None
        self._mbox = None
        self._mbox_sha1sum = None
        self._openid = None
        self._account = None
        self._member = None
        self.discriminator = None

        self.object_type = object_type
        if name is not None:
            self.name = name
        if mbox is not None:
            self.mbox = mbox
        if mbox_sha1sum is not None:
            self.mbox_sha1sum = mbox_sha1sum
        if openid is not None:
            self.openid = openid
        if account is not None:
            self.account = account
        if member is not None:
            self.member = member

    @property
    def object_type(self):
        """Gets the object_type of this XapiAgentGroup.  # noqa: E501

        allowed_values = ["Agent", "Group"]  # noqa: E501

        :return: The object_type of this XapiAgentGroup.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this XapiAgentGroup.

        allowed_values = ["Agent", "Group"]  # noqa: E501

        :param object_type: The object_type of this XapiAgentGroup.  # noqa: E501
        :type: str
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501

        self._object_type = object_type

    @property
    def name(self):
        """Gets the name of this XapiAgentGroup.  # noqa: E501

        :return: The name of this XapiAgentGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XapiAgentGroup.

        :param name: The name of this XapiAgentGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mbox(self):
        """Gets the mbox of this XapiAgentGroup.  # noqa: E501

        :return: The mbox of this XapiAgentGroup.  # noqa: E501
        :rtype: str
        """
        return self._mbox

    @mbox.setter
    def mbox(self, mbox):
        """Sets the mbox of this XapiAgentGroup.

        :param mbox: The mbox of this XapiAgentGroup.  # noqa: E501
        :type: str
        """

        self._mbox = mbox

    @property
    def mbox_sha1sum(self):
        """Gets the mbox_sha1sum of this XapiAgentGroup.  # noqa: E501

        :return: The mbox_sha1sum of this XapiAgentGroup.  # noqa: E501
        :rtype: str
        """
        return self._mbox_sha1sum

    @mbox_sha1sum.setter
    def mbox_sha1sum(self, mbox_sha1sum):
        """Sets the mbox_sha1sum of this XapiAgentGroup.

        :param mbox_sha1sum: The mbox_sha1sum of this XapiAgentGroup.  # noqa: E501
        :type: str
        """

        self._mbox_sha1sum = mbox_sha1sum

    @property
    def openid(self):
        """Gets the openid of this XapiAgentGroup.  # noqa: E501

        :return: The openid of this XapiAgentGroup.  # noqa: E501
        :rtype: str
        """
        return self._openid

    @openid.setter
    def openid(self, openid):
        """Sets the openid of this XapiAgentGroup.

        :param openid: The openid of this XapiAgentGroup.  # noqa: E501
        :type: str
        """

        self._openid = openid

    @property
    def account(self):
        """Gets the account of this XapiAgentGroup.  # noqa: E501

        :return: The account of this XapiAgentGroup.  # noqa: E501
        :rtype: XapiAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this XapiAgentGroup.

        :param account: The account of this XapiAgentGroup.  # noqa: E501
        :type: XapiAccount
        """

        self._account = account

    @property
    def member(self):
        """Gets the member of this XapiAgentGroup.  # noqa: E501

        :return: The member of this XapiAgentGroup.  # noqa: E501
        :rtype: list[XapiAgentGroup]
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this XapiAgentGroup.

        :param member: The member of this XapiAgentGroup.  # noqa: E501
        :type: list[XapiAgentGroup]
        """

        self._member = member

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
        if issubclass(XapiAgentGroup, dict):
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
        if not isinstance(other, XapiAgentGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
