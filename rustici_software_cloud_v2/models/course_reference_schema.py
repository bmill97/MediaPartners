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


class CourseReferenceSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, version=None):
        """
        CourseReferenceSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'version': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'version': 'version'
        }

        self._id = id
        self._title = title
        self._version = version

    @property
    def id(self):
        """
        Gets the id of this CourseReferenceSchema.

        :return: The id of this CourseReferenceSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CourseReferenceSchema.

        :param id: The id of this CourseReferenceSchema.
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this CourseReferenceSchema.

        :return: The title of this CourseReferenceSchema.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CourseReferenceSchema.

        :param title: The title of this CourseReferenceSchema.
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """
        Gets the version of this CourseReferenceSchema.

        :return: The version of this CourseReferenceSchema.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CourseReferenceSchema.

        :param version: The version of this CourseReferenceSchema.
        :type: int
        """

        self._version = version

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
        if not isinstance(other, CourseReferenceSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
