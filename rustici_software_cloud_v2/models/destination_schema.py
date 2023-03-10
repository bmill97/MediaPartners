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


class DestinationSchema(object):
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
        'name': 'str',
        'updated': 'datetime',
        'created': 'datetime',
        'tags': 'list[str]',
        'email': 'str',
        'notes': 'str',
        'launch_auth': 'LaunchAuthSchema',
        'lti13_data': 'Lti13PlatformConfigurationSchema'
    }

    attribute_map = {
        'name': 'name',
        'updated': 'updated',
        'created': 'created',
        'tags': 'tags',
        'email': 'email',
        'notes': 'notes',
        'launch_auth': 'launchAuth',
        'lti13_data': 'lti13Data'
    }

    def __init__(self, name=None, updated=None, created=None, tags=None, email=None, notes=None, launch_auth=None, lti13_data=None):  # noqa: E501
        """DestinationSchema - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._updated = None
        self._created = None
        self._tags = None
        self._email = None
        self._notes = None
        self._launch_auth = None
        self._lti13_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if updated is not None:
            self.updated = updated
        if created is not None:
            self.created = created
        if tags is not None:
            self.tags = tags
        if email is not None:
            self.email = email
        if notes is not None:
            self.notes = notes
        if launch_auth is not None:
            self.launch_auth = launch_auth
        if lti13_data is not None:
            self.lti13_data = lti13_data

    @property
    def name(self):
        """Gets the name of this DestinationSchema.  # noqa: E501

        The destination's name.  # noqa: E501

        :return: The name of this DestinationSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DestinationSchema.

        The destination's name.  # noqa: E501

        :param name: The name of this DestinationSchema.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def updated(self):
        """Gets the updated of this DestinationSchema.  # noqa: E501

        :return: The updated of this DestinationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DestinationSchema.

        :param updated: The updated of this DestinationSchema.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def created(self):
        """Gets the created of this DestinationSchema.  # noqa: E501

        :return: The created of this DestinationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DestinationSchema.

        :param created: The created of this DestinationSchema.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def tags(self):
        """Gets the tags of this DestinationSchema.  # noqa: E501

        Optional array of tags.  # noqa: E501

        :return: The tags of this DestinationSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DestinationSchema.

        Optional array of tags.  # noqa: E501

        :param tags: The tags of this DestinationSchema.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def email(self):
        """Gets the email of this DestinationSchema.  # noqa: E501

        SCORM Cloud user e-mail associated with this destination. If this is not provided, it will default to the owner of the Realm.   # noqa: E501

        :return: The email of this DestinationSchema.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this DestinationSchema.

        SCORM Cloud user e-mail associated with this destination. If this is not provided, it will default to the owner of the Realm.   # noqa: E501

        :param email: The email of this DestinationSchema.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def notes(self):
        """Gets the notes of this DestinationSchema.  # noqa: E501

        Any provided notes about this Destination  # noqa: E501

        :return: The notes of this DestinationSchema.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this DestinationSchema.

        Any provided notes about this Destination  # noqa: E501

        :param notes: The notes of this DestinationSchema.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def launch_auth(self):
        """Gets the launch_auth of this DestinationSchema.  # noqa: E501

        :return: The launch_auth of this DestinationSchema.  # noqa: E501
        :rtype: LaunchAuthSchema
        """
        return self._launch_auth

    @launch_auth.setter
    def launch_auth(self, launch_auth):
        """Sets the launch_auth of this DestinationSchema.

        :param launch_auth: The launch_auth of this DestinationSchema.  # noqa: E501
        :type: LaunchAuthSchema
        """

        self._launch_auth = launch_auth

    @property
    def lti13_data(self):
        """Gets the lti13_data of this DestinationSchema.  # noqa: E501

        :return: The lti13_data of this DestinationSchema.  # noqa: E501
        :rtype: Lti13PlatformConfigurationSchema
        """
        return self._lti13_data

    @lti13_data.setter
    def lti13_data(self, lti13_data):
        """Sets the lti13_data of this DestinationSchema.

        :param lti13_data: The lti13_data of this DestinationSchema.  # noqa: E501
        :type: Lti13PlatformConfigurationSchema
        """

        self._lti13_data = lti13_data

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
        if issubclass(DestinationSchema, dict):
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
        if not isinstance(other, DestinationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
