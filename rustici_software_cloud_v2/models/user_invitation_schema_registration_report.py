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


class UserInvitationSchemaRegistrationReport(object):
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
        'complete': 'RegistrationCompletion',
        'success': 'RegistrationSuccess',
        'total_seconds_tracked': 'float',
        'score': 'ScoreSchema'
    }

    attribute_map = {
        'complete': 'complete',
        'success': 'success',
        'total_seconds_tracked': 'totalSecondsTracked',
        'score': 'score'
    }

    def __init__(self, complete=None, success=None, total_seconds_tracked=None, score=None):  # noqa: E501
        """UserInvitationSchemaRegistrationReport - a model defined in Swagger"""  # noqa: E501

        self._complete = None
        self._success = None
        self._total_seconds_tracked = None
        self._score = None
        self.discriminator = None

        if complete is not None:
            self.complete = complete
        if success is not None:
            self.success = success
        if total_seconds_tracked is not None:
            self.total_seconds_tracked = total_seconds_tracked
        if score is not None:
            self.score = score

    @property
    def complete(self):
        """Gets the complete of this UserInvitationSchemaRegistrationReport.  # noqa: E501

        :return: The complete of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :rtype: RegistrationCompletion
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this UserInvitationSchemaRegistrationReport.

        :param complete: The complete of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :type: RegistrationCompletion
        """

        self._complete = complete

    @property
    def success(self):
        """Gets the success of this UserInvitationSchemaRegistrationReport.  # noqa: E501

        :return: The success of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :rtype: RegistrationSuccess
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UserInvitationSchemaRegistrationReport.

        :param success: The success of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :type: RegistrationSuccess
        """

        self._success = success

    @property
    def total_seconds_tracked(self):
        """Gets the total_seconds_tracked of this UserInvitationSchemaRegistrationReport.  # noqa: E501

        :return: The total_seconds_tracked of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :rtype: float
        """
        return self._total_seconds_tracked

    @total_seconds_tracked.setter
    def total_seconds_tracked(self, total_seconds_tracked):
        """Sets the total_seconds_tracked of this UserInvitationSchemaRegistrationReport.

        :param total_seconds_tracked: The total_seconds_tracked of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :type: float
        """

        self._total_seconds_tracked = total_seconds_tracked

    @property
    def score(self):
        """Gets the score of this UserInvitationSchemaRegistrationReport.  # noqa: E501

        :return: The score of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :rtype: ScoreSchema
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this UserInvitationSchemaRegistrationReport.

        :param score: The score of this UserInvitationSchemaRegistrationReport.  # noqa: E501
        :type: ScoreSchema
        """

        self._score = score

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
        if issubclass(UserInvitationSchemaRegistrationReport, dict):
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
        if not isinstance(other, UserInvitationSchemaRegistrationReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
