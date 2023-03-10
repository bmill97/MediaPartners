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


class CourseActivitySchema(object):
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
        'external_identifier': 'str',
        'item_identifier': 'str',
        'resource_identifier': 'str',
        'activity_type': 'str',
        'href': 'str',
        'scaled_passing_score': 'str',
        'title': 'str',
        'children': 'list[CourseActivitySchema]'
    }

    attribute_map = {
        'external_identifier': 'externalIdentifier',
        'item_identifier': 'itemIdentifier',
        'resource_identifier': 'resourceIdentifier',
        'activity_type': 'activityType',
        'href': 'href',
        'scaled_passing_score': 'scaledPassingScore',
        'title': 'title',
        'children': 'children'
    }

    def __init__(self, external_identifier=None, item_identifier=None, resource_identifier=None, activity_type=None, href=None, scaled_passing_score=None, title=None, children=None):  # noqa: E501
        """CourseActivitySchema - a model defined in Swagger"""  # noqa: E501

        self._external_identifier = None
        self._item_identifier = None
        self._resource_identifier = None
        self._activity_type = None
        self._href = None
        self._scaled_passing_score = None
        self._title = None
        self._children = None
        self.discriminator = None

        if external_identifier is not None:
            self.external_identifier = external_identifier
        if item_identifier is not None:
            self.item_identifier = item_identifier
        if resource_identifier is not None:
            self.resource_identifier = resource_identifier
        if activity_type is not None:
            self.activity_type = activity_type
        if href is not None:
            self.href = href
        if scaled_passing_score is not None:
            self.scaled_passing_score = scaled_passing_score
        if title is not None:
            self.title = title
        if children is not None:
            self.children = children

    @property
    def external_identifier(self):
        """Gets the external_identifier of this CourseActivitySchema.  # noqa: E501

        An arbitrary identifier that the external LMS system can associate with this LearningObject to track it as it is reused across courses   # noqa: E501

        :return: The external_identifier of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this CourseActivitySchema.

        An arbitrary identifier that the external LMS system can associate with this LearningObject to track it as it is reused across courses   # noqa: E501

        :param external_identifier: The external_identifier of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def item_identifier(self):
        """Gets the item_identifier of this CourseActivitySchema.  # noqa: E501

        The string which identifies this activity in the context of its course  # noqa: E501

        :return: The item_identifier of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._item_identifier

    @item_identifier.setter
    def item_identifier(self, item_identifier):
        """Sets the item_identifier of this CourseActivitySchema.

        The string which identifies this activity in the context of its course  # noqa: E501

        :param item_identifier: The item_identifier of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._item_identifier = item_identifier

    @property
    def resource_identifier(self):
        """Gets the resource_identifier of this CourseActivitySchema.  # noqa: E501

        The string which identifies this activity's resource in a course's manifest  # noqa: E501

        :return: The resource_identifier of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._resource_identifier

    @resource_identifier.setter
    def resource_identifier(self, resource_identifier):
        """Sets the resource_identifier of this CourseActivitySchema.

        The string which identifies this activity's resource in a course's manifest  # noqa: E501

        :param resource_identifier: The resource_identifier of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._resource_identifier = resource_identifier

    @property
    def activity_type(self):
        """Gets the activity_type of this CourseActivitySchema.  # noqa: E501

        The type of activity this is  # noqa: E501

        allowed_values = ["UNKNOWN", "AGGREGATION", "SCO", "ASSET", "OBJECTIVE"]  # noqa: E501

        :return: The activity_type of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this CourseActivitySchema.

        The type of activity this is  # noqa: E501

        allowed_values = ["UNKNOWN", "AGGREGATION", "SCO", "ASSET", "OBJECTIVE"]  # noqa: E501

        :param activity_type: The activity_type of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._activity_type = activity_type

    @property
    def href(self):
        """Gets the href of this CourseActivitySchema.  # noqa: E501

        The web path used to launch this activity  # noqa: E501

        :return: The href of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CourseActivitySchema.

        The web path used to launch this activity  # noqa: E501

        :param href: The href of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def scaled_passing_score(self):
        """Gets the scaled_passing_score of this CourseActivitySchema.  # noqa: E501

        The score required of a learner to pass this activity  # noqa: E501

        :return: The scaled_passing_score of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._scaled_passing_score

    @scaled_passing_score.setter
    def scaled_passing_score(self, scaled_passing_score):
        """Sets the scaled_passing_score of this CourseActivitySchema.

        The score required of a learner to pass this activity  # noqa: E501

        :param scaled_passing_score: The scaled_passing_score of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._scaled_passing_score = scaled_passing_score

    @property
    def title(self):
        """Gets the title of this CourseActivitySchema.  # noqa: E501

        The title of the activity  # noqa: E501

        :return: The title of this CourseActivitySchema.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CourseActivitySchema.

        The title of the activity  # noqa: E501

        :param title: The title of this CourseActivitySchema.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def children(self):
        """Gets the children of this CourseActivitySchema.  # noqa: E501

        :return: The children of this CourseActivitySchema.  # noqa: E501
        :rtype: list[CourseActivitySchema]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this CourseActivitySchema.

        :param children: The children of this CourseActivitySchema.  # noqa: E501
        :type: list[CourseActivitySchema]
        """

        self._children = children

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
        if issubclass(CourseActivitySchema, dict):
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
        if not isinstance(other, CourseActivitySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
