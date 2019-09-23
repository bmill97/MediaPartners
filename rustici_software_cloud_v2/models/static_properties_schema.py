# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StaticPropertiesSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, completion_threshold=None, launch_data=None, max_time_allowed=None, scaled_passing_score=None, scaled_passing_score_used=None, time_limit_action=None):
        """
        StaticPropertiesSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'completion_threshold': 'str',
            'launch_data': 'str',
            'max_time_allowed': 'str',
            'scaled_passing_score': 'float',
            'scaled_passing_score_used': 'bool',
            'time_limit_action': 'str'
        }

        self.attribute_map = {
            'completion_threshold': 'completionThreshold',
            'launch_data': 'launchData',
            'max_time_allowed': 'maxTimeAllowed',
            'scaled_passing_score': 'scaledPassingScore',
            'scaled_passing_score_used': 'scaledPassingScoreUsed',
            'time_limit_action': 'timeLimitAction'
        }

        self._completion_threshold = completion_threshold
        self._launch_data = launch_data
        self._max_time_allowed = max_time_allowed
        self._scaled_passing_score = scaled_passing_score
        self._scaled_passing_score_used = scaled_passing_score_used
        self._time_limit_action = time_limit_action

    @property
    def completion_threshold(self):
        """
        Gets the completion_threshold of this StaticPropertiesSchema.

        :return: The completion_threshold of this StaticPropertiesSchema.
        :rtype: str
        """
        return self._completion_threshold

    @completion_threshold.setter
    def completion_threshold(self, completion_threshold):
        """
        Sets the completion_threshold of this StaticPropertiesSchema.

        :param completion_threshold: The completion_threshold of this StaticPropertiesSchema.
        :type: str
        """

        self._completion_threshold = completion_threshold

    @property
    def launch_data(self):
        """
        Gets the launch_data of this StaticPropertiesSchema.

        :return: The launch_data of this StaticPropertiesSchema.
        :rtype: str
        """
        return self._launch_data

    @launch_data.setter
    def launch_data(self, launch_data):
        """
        Sets the launch_data of this StaticPropertiesSchema.

        :param launch_data: The launch_data of this StaticPropertiesSchema.
        :type: str
        """

        self._launch_data = launch_data

    @property
    def max_time_allowed(self):
        """
        Gets the max_time_allowed of this StaticPropertiesSchema.

        :return: The max_time_allowed of this StaticPropertiesSchema.
        :rtype: str
        """
        return self._max_time_allowed

    @max_time_allowed.setter
    def max_time_allowed(self, max_time_allowed):
        """
        Sets the max_time_allowed of this StaticPropertiesSchema.

        :param max_time_allowed: The max_time_allowed of this StaticPropertiesSchema.
        :type: str
        """

        self._max_time_allowed = max_time_allowed

    @property
    def scaled_passing_score(self):
        """
        Gets the scaled_passing_score of this StaticPropertiesSchema.

        :return: The scaled_passing_score of this StaticPropertiesSchema.
        :rtype: float
        """
        return self._scaled_passing_score

    @scaled_passing_score.setter
    def scaled_passing_score(self, scaled_passing_score):
        """
        Sets the scaled_passing_score of this StaticPropertiesSchema.

        :param scaled_passing_score: The scaled_passing_score of this StaticPropertiesSchema.
        :type: float
        """

        self._scaled_passing_score = scaled_passing_score

    @property
    def scaled_passing_score_used(self):
        """
        Gets the scaled_passing_score_used of this StaticPropertiesSchema.

        :return: The scaled_passing_score_used of this StaticPropertiesSchema.
        :rtype: bool
        """
        return self._scaled_passing_score_used

    @scaled_passing_score_used.setter
    def scaled_passing_score_used(self, scaled_passing_score_used):
        """
        Sets the scaled_passing_score_used of this StaticPropertiesSchema.

        :param scaled_passing_score_used: The scaled_passing_score_used of this StaticPropertiesSchema.
        :type: bool
        """

        self._scaled_passing_score_used = scaled_passing_score_used

    @property
    def time_limit_action(self):
        """
        Gets the time_limit_action of this StaticPropertiesSchema.

        :return: The time_limit_action of this StaticPropertiesSchema.
        :rtype: str
        """
        return self._time_limit_action

    @time_limit_action.setter
    def time_limit_action(self, time_limit_action):
        """
        Sets the time_limit_action of this StaticPropertiesSchema.

        :param time_limit_action: The time_limit_action of this StaticPropertiesSchema.
        :type: str
        """

        self._time_limit_action = time_limit_action

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, StaticPropertiesSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
