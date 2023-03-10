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


class XapiContext(object):
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
        'registration': 'str',
        'instructor': 'XapiAgentGroup',
        'team': 'XapiAgentGroup',
        'context_activities': 'XapiContextActivity',
        'revision': 'str',
        'platform': 'str',
        'language': 'str',
        'statement': 'XapiStatementReference',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'registration': 'registration',
        'instructor': 'instructor',
        'team': 'team',
        'context_activities': 'contextActivities',
        'revision': 'revision',
        'platform': 'platform',
        'language': 'language',
        'statement': 'statement',
        'extensions': 'extensions'
    }

    def __init__(self, registration=None, instructor=None, team=None, context_activities=None, revision=None, platform=None, language=None, statement=None, extensions=None):  # noqa: E501
        """XapiContext - a model defined in Swagger"""  # noqa: E501

        self._registration = None
        self._instructor = None
        self._team = None
        self._context_activities = None
        self._revision = None
        self._platform = None
        self._language = None
        self._statement = None
        self._extensions = None
        self.discriminator = None

        if registration is not None:
            self.registration = registration
        if instructor is not None:
            self.instructor = instructor
        if team is not None:
            self.team = team
        if context_activities is not None:
            self.context_activities = context_activities
        if revision is not None:
            self.revision = revision
        if platform is not None:
            self.platform = platform
        if language is not None:
            self.language = language
        if statement is not None:
            self.statement = statement
        if extensions is not None:
            self.extensions = extensions

    @property
    def registration(self):
        """Gets the registration of this XapiContext.  # noqa: E501

        :return: The registration of this XapiContext.  # noqa: E501
        :rtype: str
        """
        return self._registration

    @registration.setter
    def registration(self, registration):
        """Sets the registration of this XapiContext.

        :param registration: The registration of this XapiContext.  # noqa: E501
        :type: str
        """

        self._registration = registration

    @property
    def instructor(self):
        """Gets the instructor of this XapiContext.  # noqa: E501

        :return: The instructor of this XapiContext.  # noqa: E501
        :rtype: XapiAgentGroup
        """
        return self._instructor

    @instructor.setter
    def instructor(self, instructor):
        """Sets the instructor of this XapiContext.

        :param instructor: The instructor of this XapiContext.  # noqa: E501
        :type: XapiAgentGroup
        """

        self._instructor = instructor

    @property
    def team(self):
        """Gets the team of this XapiContext.  # noqa: E501

        :return: The team of this XapiContext.  # noqa: E501
        :rtype: XapiAgentGroup
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this XapiContext.

        :param team: The team of this XapiContext.  # noqa: E501
        :type: XapiAgentGroup
        """

        self._team = team

    @property
    def context_activities(self):
        """Gets the context_activities of this XapiContext.  # noqa: E501

        :return: The context_activities of this XapiContext.  # noqa: E501
        :rtype: XapiContextActivity
        """
        return self._context_activities

    @context_activities.setter
    def context_activities(self, context_activities):
        """Sets the context_activities of this XapiContext.

        :param context_activities: The context_activities of this XapiContext.  # noqa: E501
        :type: XapiContextActivity
        """

        self._context_activities = context_activities

    @property
    def revision(self):
        """Gets the revision of this XapiContext.  # noqa: E501

        :return: The revision of this XapiContext.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this XapiContext.

        :param revision: The revision of this XapiContext.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def platform(self):
        """Gets the platform of this XapiContext.  # noqa: E501

        :return: The platform of this XapiContext.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this XapiContext.

        :param platform: The platform of this XapiContext.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def language(self):
        """Gets the language of this XapiContext.  # noqa: E501

        :return: The language of this XapiContext.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this XapiContext.

        :param language: The language of this XapiContext.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def statement(self):
        """Gets the statement of this XapiContext.  # noqa: E501

        :return: The statement of this XapiContext.  # noqa: E501
        :rtype: XapiStatementReference
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this XapiContext.

        :param statement: The statement of this XapiContext.  # noqa: E501
        :type: XapiStatementReference
        """

        self._statement = statement

    @property
    def extensions(self):
        """Gets the extensions of this XapiContext.  # noqa: E501

        :return: The extensions of this XapiContext.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this XapiContext.

        :param extensions: The extensions of this XapiContext.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if issubclass(XapiContext, dict):
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
        if not isinstance(other, XapiContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
