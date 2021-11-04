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


class PublicInvitationUpdateSchema(object):
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
        'allow_launch': 'bool',
        'allow_new_registrations': 'bool',
        'post_back': 'PostBackSchema',
        'expiration_date': 'datetime',
        'registration_cap': 'int'
    }

    attribute_map = {
        'allow_launch': 'allowLaunch',
        'allow_new_registrations': 'allowNewRegistrations',
        'post_back': 'postBack',
        'expiration_date': 'expirationDate',
        'registration_cap': 'registrationCap'
    }

    def __init__(self, allow_launch=None, allow_new_registrations=None, post_back=None, expiration_date=None, registration_cap=0):  # noqa: E501
        """PublicInvitationUpdateSchema - a model defined in Swagger"""  # noqa: E501

        self._allow_launch = None
        self._allow_new_registrations = None
        self._post_back = None
        self._expiration_date = None
        self._registration_cap = None
        self.discriminator = None

        if allow_launch is not None:
            self.allow_launch = allow_launch
        if allow_new_registrations is not None:
            self.allow_new_registrations = allow_new_registrations
        if post_back is not None:
            self.post_back = post_back
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if registration_cap is not None:
            self.registration_cap = registration_cap

    @property
    def allow_launch(self):
        """Gets the allow_launch of this PublicInvitationUpdateSchema.  # noqa: E501

        If true, then new registrations can be created for this invitation.  # noqa: E501

        :return: The allow_launch of this PublicInvitationUpdateSchema.  # noqa: E501
        :rtype: bool
        """
        return self._allow_launch

    @allow_launch.setter
    def allow_launch(self, allow_launch):
        """Sets the allow_launch of this PublicInvitationUpdateSchema.

        If true, then new registrations can be created for this invitation.  # noqa: E501

        :param allow_launch: The allow_launch of this PublicInvitationUpdateSchema.  # noqa: E501
        :type: bool
        """

        self._allow_launch = allow_launch

    @property
    def allow_new_registrations(self):
        """Gets the allow_new_registrations of this PublicInvitationUpdateSchema.  # noqa: E501

        If true, then new registrations can be created for this invitation.  # noqa: E501

        :return: The allow_new_registrations of this PublicInvitationUpdateSchema.  # noqa: E501
        :rtype: bool
        """
        return self._allow_new_registrations

    @allow_new_registrations.setter
    def allow_new_registrations(self, allow_new_registrations):
        """Sets the allow_new_registrations of this PublicInvitationUpdateSchema.

        If true, then new registrations can be created for this invitation.  # noqa: E501

        :param allow_new_registrations: The allow_new_registrations of this PublicInvitationUpdateSchema.  # noqa: E501
        :type: bool
        """

        self._allow_new_registrations = allow_new_registrations

    @property
    def post_back(self):
        """Gets the post_back of this PublicInvitationUpdateSchema.  # noqa: E501

        Specifies a URL for which to post activity and status data in real time as the course is completed  # noqa: E501

        :return: The post_back of this PublicInvitationUpdateSchema.  # noqa: E501
        :rtype: PostBackSchema
        """
        return self._post_back

    @post_back.setter
    def post_back(self, post_back):
        """Sets the post_back of this PublicInvitationUpdateSchema.

        Specifies a URL for which to post activity and status data in real time as the course is completed  # noqa: E501

        :param post_back: The post_back of this PublicInvitationUpdateSchema.  # noqa: E501
        :type: PostBackSchema
        """

        self._post_back = post_back

    @property
    def expiration_date(self):
        """Gets the expiration_date of this PublicInvitationUpdateSchema.  # noqa: E501

        The ISO 8601 TimeStamp (defaults to UTC) after which this invitation will expire and can no longer be launched. An empty value will represent no expiration date.   # noqa: E501

        :return: The expiration_date of this PublicInvitationUpdateSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this PublicInvitationUpdateSchema.

        The ISO 8601 TimeStamp (defaults to UTC) after which this invitation will expire and can no longer be launched. An empty value will represent no expiration date.   # noqa: E501

        :param expiration_date: The expiration_date of this PublicInvitationUpdateSchema.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def registration_cap(self):
        """Gets the registration_cap of this PublicInvitationUpdateSchema.  # noqa: E501

        Integer value that limits the amount of registrations a public invitation can generate.  # noqa: E501

        :return: The registration_cap of this PublicInvitationUpdateSchema.  # noqa: E501
        :rtype: int
        """
        return self._registration_cap

    @registration_cap.setter
    def registration_cap(self, registration_cap):
        """Sets the registration_cap of this PublicInvitationUpdateSchema.

        Integer value that limits the amount of registrations a public invitation can generate.  # noqa: E501

        :param registration_cap: The registration_cap of this PublicInvitationUpdateSchema.  # noqa: E501
        :type: int
        """

        self._registration_cap = registration_cap

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
        if issubclass(PublicInvitationUpdateSchema, dict):
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
        if not isinstance(other, PublicInvitationUpdateSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
