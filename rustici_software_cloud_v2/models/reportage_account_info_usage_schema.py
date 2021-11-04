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


class ReportageAccountInfoUsageSchema(object):
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
        'month_start': 'datetime',
        'reg_count': 'int',
        'total_registrations': 'int',
        'total_courses': 'int'
    }

    attribute_map = {
        'month_start': 'monthStart',
        'reg_count': 'regCount',
        'total_registrations': 'totalRegistrations',
        'total_courses': 'totalCourses'
    }

    def __init__(self, month_start=None, reg_count=None, total_registrations=None, total_courses=None):  # noqa: E501
        """ReportageAccountInfoUsageSchema - a model defined in Swagger"""  # noqa: E501

        self._month_start = None
        self._reg_count = None
        self._total_registrations = None
        self._total_courses = None
        self.discriminator = None

        if month_start is not None:
            self.month_start = month_start
        if reg_count is not None:
            self.reg_count = reg_count
        if total_registrations is not None:
            self.total_registrations = total_registrations
        if total_courses is not None:
            self.total_courses = total_courses

    @property
    def month_start(self):
        """Gets the month_start of this ReportageAccountInfoUsageSchema.  # noqa: E501

        :return: The month_start of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._month_start

    @month_start.setter
    def month_start(self, month_start):
        """Sets the month_start of this ReportageAccountInfoUsageSchema.

        :param month_start: The month_start of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :type: datetime
        """

        self._month_start = month_start

    @property
    def reg_count(self):
        """Gets the reg_count of this ReportageAccountInfoUsageSchema.  # noqa: E501

        :return: The reg_count of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :rtype: int
        """
        return self._reg_count

    @reg_count.setter
    def reg_count(self, reg_count):
        """Sets the reg_count of this ReportageAccountInfoUsageSchema.

        :param reg_count: The reg_count of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :type: int
        """

        self._reg_count = reg_count

    @property
    def total_registrations(self):
        """Gets the total_registrations of this ReportageAccountInfoUsageSchema.  # noqa: E501

        :return: The total_registrations of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_registrations

    @total_registrations.setter
    def total_registrations(self, total_registrations):
        """Sets the total_registrations of this ReportageAccountInfoUsageSchema.

        :param total_registrations: The total_registrations of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :type: int
        """

        self._total_registrations = total_registrations

    @property
    def total_courses(self):
        """Gets the total_courses of this ReportageAccountInfoUsageSchema.  # noqa: E501

        :return: The total_courses of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_courses

    @total_courses.setter
    def total_courses(self, total_courses):
        """Sets the total_courses of this ReportageAccountInfoUsageSchema.

        :param total_courses: The total_courses of this ReportageAccountInfoUsageSchema.  # noqa: E501
        :type: int
        """

        self._total_courses = total_courses

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
        if issubclass(ReportageAccountInfoUsageSchema, dict):
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
        if not isinstance(other, ReportageAccountInfoUsageSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
