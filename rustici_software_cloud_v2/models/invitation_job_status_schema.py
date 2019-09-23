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


class InvitationJobStatusSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, errors=None, total=None, processed=None):
        """
        InvitationJobStatusSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'errors': 'list[str]',
            'total': 'int',
            'processed': 'int'
        }

        self.attribute_map = {
            'status': 'status',
            'errors': 'errors',
            'total': 'total',
            'processed': 'processed'
        }

        self._status = status
        self._errors = errors
        self._total = total
        self._processed = processed

    @property
    def status(self):
        """
        Gets the status of this InvitationJobStatusSchema.
        The status of the job.

        :return: The status of this InvitationJobStatusSchema.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InvitationJobStatusSchema.
        The status of the job.

        :param status: The status of this InvitationJobStatusSchema.
        :type: str
        """
        allowed_values = ["STARTED", "CANCELLED", "COMPLETE", "ERROR"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def errors(self):
        """
        Gets the errors of this InvitationJobStatusSchema.
        An array containing any errors which occurred.

        :return: The errors of this InvitationJobStatusSchema.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this InvitationJobStatusSchema.
        An array containing any errors which occurred.

        :param errors: The errors of this InvitationJobStatusSchema.
        :type: list[str]
        """

        self._errors = errors

    @property
    def total(self):
        """
        Gets the total of this InvitationJobStatusSchema.
        The total number of private invitations to be sent.

        :return: The total of this InvitationJobStatusSchema.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this InvitationJobStatusSchema.
        The total number of private invitations to be sent.

        :param total: The total of this InvitationJobStatusSchema.
        :type: int
        """

        self._total = total

    @property
    def processed(self):
        """
        Gets the processed of this InvitationJobStatusSchema.
        The number of private invitations which have been sent.

        :return: The processed of this InvitationJobStatusSchema.
        :rtype: int
        """
        return self._processed

    @processed.setter
    def processed(self, processed):
        """
        Sets the processed of this InvitationJobStatusSchema.
        The number of private invitations which have been sent.

        :param processed: The processed of this InvitationJobStatusSchema.
        :type: int
        """

        self._processed = processed

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
        if not isinstance(other, InvitationJobStatusSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
