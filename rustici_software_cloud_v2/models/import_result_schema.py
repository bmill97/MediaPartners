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


class ImportResultSchema(object):
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
        'web_path_to_course': 'str',
        'parser_warnings': 'list[str]',
        'course_languages': 'list[str]',
        'course': 'CourseSchema'
    }

    attribute_map = {
        'web_path_to_course': 'webPathToCourse',
        'parser_warnings': 'parserWarnings',
        'course_languages': 'courseLanguages',
        'course': 'course'
    }

    def __init__(self, web_path_to_course=None, parser_warnings=None, course_languages=None, course=None):  # noqa: E501
        """ImportResultSchema - a model defined in Swagger"""  # noqa: E501

        self._web_path_to_course = None
        self._parser_warnings = None
        self._course_languages = None
        self._course = None
        self.discriminator = None

        if web_path_to_course is not None:
            self.web_path_to_course = web_path_to_course
        if parser_warnings is not None:
            self.parser_warnings = parser_warnings
        if course_languages is not None:
            self.course_languages = course_languages
        if course is not None:
            self.course = course

    @property
    def web_path_to_course(self):
        """Gets the web_path_to_course of this ImportResultSchema.  # noqa: E501

        web path to this course  # noqa: E501

        :return: The web_path_to_course of this ImportResultSchema.  # noqa: E501
        :rtype: str
        """
        return self._web_path_to_course

    @web_path_to_course.setter
    def web_path_to_course(self, web_path_to_course):
        """Sets the web_path_to_course of this ImportResultSchema.

        web path to this course  # noqa: E501

        :param web_path_to_course: The web_path_to_course of this ImportResultSchema.  # noqa: E501
        :type: str
        """

        self._web_path_to_course = web_path_to_course

    @property
    def parser_warnings(self):
        """Gets the parser_warnings of this ImportResultSchema.  # noqa: E501

        :return: The parser_warnings of this ImportResultSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._parser_warnings

    @parser_warnings.setter
    def parser_warnings(self, parser_warnings):
        """Sets the parser_warnings of this ImportResultSchema.

        :param parser_warnings: The parser_warnings of this ImportResultSchema.  # noqa: E501
        :type: list[str]
        """

        self._parser_warnings = parser_warnings

    @property
    def course_languages(self):
        """Gets the course_languages of this ImportResultSchema.  # noqa: E501

        :return: The course_languages of this ImportResultSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._course_languages

    @course_languages.setter
    def course_languages(self, course_languages):
        """Sets the course_languages of this ImportResultSchema.

        :param course_languages: The course_languages of this ImportResultSchema.  # noqa: E501
        :type: list[str]
        """

        self._course_languages = course_languages

    @property
    def course(self):
        """Gets the course of this ImportResultSchema.  # noqa: E501

        :return: The course of this ImportResultSchema.  # noqa: E501
        :rtype: CourseSchema
        """
        return self._course

    @course.setter
    def course(self, course):
        """Sets the course of this ImportResultSchema.

        :param course: The course of this ImportResultSchema.  # noqa: E501
        :type: CourseSchema
        """

        self._course = course

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
        if issubclass(ImportResultSchema, dict):
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
        if not isinstance(other, ImportResultSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
