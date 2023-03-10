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


class RuntimeInteractionSchema(object):
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
        'id': 'str',
        'type': 'str',
        'objectives': 'list[str]',
        'timestamp': 'str',
        'timestamp_utc': 'str',
        'correct_responses': 'list[str]',
        'weighting': 'str',
        'learner_response': 'str',
        'result': 'str',
        'latency': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'objectives': 'objectives',
        'timestamp': 'timestamp',
        'timestamp_utc': 'timestampUtc',
        'correct_responses': 'correctResponses',
        'weighting': 'weighting',
        'learner_response': 'learnerResponse',
        'result': 'result',
        'latency': 'latency',
        'description': 'description'
    }

    def __init__(self, id=None, type=None, objectives=None, timestamp=None, timestamp_utc=None, correct_responses=None, weighting=None, learner_response=None, result=None, latency=None, description=None):  # noqa: E501
        """RuntimeInteractionSchema - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._objectives = None
        self._timestamp = None
        self._timestamp_utc = None
        self._correct_responses = None
        self._weighting = None
        self._learner_response = None
        self._result = None
        self._latency = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if objectives is not None:
            self.objectives = objectives
        if timestamp is not None:
            self.timestamp = timestamp
        if timestamp_utc is not None:
            self.timestamp_utc = timestamp_utc
        if correct_responses is not None:
            self.correct_responses = correct_responses
        if weighting is not None:
            self.weighting = weighting
        if learner_response is not None:
            self.learner_response = learner_response
        if result is not None:
            self.result = result
        if latency is not None:
            self.latency = latency
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this RuntimeInteractionSchema.  # noqa: E501

        :return: The id of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuntimeInteractionSchema.

        :param id: The id of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this RuntimeInteractionSchema.  # noqa: E501

        allowed_values = ["TrueFalse", "Choice", "FillIn", "LongFillIn", "Likert", "Matching", "Performance", "Sequencing", "Numeric", "Other"]  # noqa: E501

        :return: The type of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuntimeInteractionSchema.

        allowed_values = ["TrueFalse", "Choice", "FillIn", "LongFillIn", "Likert", "Matching", "Performance", "Sequencing", "Numeric", "Other"]  # noqa: E501

        :param type: The type of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def objectives(self):
        """Gets the objectives of this RuntimeInteractionSchema.  # noqa: E501

        :return: The objectives of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._objectives

    @objectives.setter
    def objectives(self, objectives):
        """Sets the objectives of this RuntimeInteractionSchema.

        :param objectives: The objectives of this RuntimeInteractionSchema.  # noqa: E501
        :type: list[str]
        """

        self._objectives = objectives

    @property
    def timestamp(self):
        """Gets the timestamp of this RuntimeInteractionSchema.  # noqa: E501

        :return: The timestamp of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RuntimeInteractionSchema.

        :param timestamp: The timestamp of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def timestamp_utc(self):
        """Gets the timestamp_utc of this RuntimeInteractionSchema.  # noqa: E501

        :return: The timestamp_utc of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._timestamp_utc

    @timestamp_utc.setter
    def timestamp_utc(self, timestamp_utc):
        """Sets the timestamp_utc of this RuntimeInteractionSchema.

        :param timestamp_utc: The timestamp_utc of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._timestamp_utc = timestamp_utc

    @property
    def correct_responses(self):
        """Gets the correct_responses of this RuntimeInteractionSchema.  # noqa: E501

        :return: The correct_responses of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._correct_responses

    @correct_responses.setter
    def correct_responses(self, correct_responses):
        """Sets the correct_responses of this RuntimeInteractionSchema.

        :param correct_responses: The correct_responses of this RuntimeInteractionSchema.  # noqa: E501
        :type: list[str]
        """

        self._correct_responses = correct_responses

    @property
    def weighting(self):
        """Gets the weighting of this RuntimeInteractionSchema.  # noqa: E501

        :return: The weighting of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._weighting

    @weighting.setter
    def weighting(self, weighting):
        """Sets the weighting of this RuntimeInteractionSchema.

        :param weighting: The weighting of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._weighting = weighting

    @property
    def learner_response(self):
        """Gets the learner_response of this RuntimeInteractionSchema.  # noqa: E501

        :return: The learner_response of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._learner_response

    @learner_response.setter
    def learner_response(self, learner_response):
        """Sets the learner_response of this RuntimeInteractionSchema.

        :param learner_response: The learner_response of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._learner_response = learner_response

    @property
    def result(self):
        """Gets the result of this RuntimeInteractionSchema.  # noqa: E501

        :return: The result of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RuntimeInteractionSchema.

        :param result: The result of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def latency(self):
        """Gets the latency of this RuntimeInteractionSchema.  # noqa: E501

        :return: The latency of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this RuntimeInteractionSchema.

        :param latency: The latency of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._latency = latency

    @property
    def description(self):
        """Gets the description of this RuntimeInteractionSchema.  # noqa: E501

        :return: The description of this RuntimeInteractionSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RuntimeInteractionSchema.

        :param description: The description of this RuntimeInteractionSchema.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(RuntimeInteractionSchema, dict):
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
        if not isinstance(other, RuntimeInteractionSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
