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


class ReportageAccountInfoSchema(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'company': 'str',
        'account_type': 'str',
        'reg_limit': 'int',
        'strict_limit': 'bool',
        'create_date': 'datetime',
        'usage': 'ReportageAccountInfoUsageSchema'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company': 'company',
        'account_type': 'accountType',
        'reg_limit': 'regLimit',
        'strict_limit': 'strictLimit',
        'create_date': 'createDate',
        'usage': 'usage'
    }

    def __init__(self, email=None, first_name=None, last_name=None, company=None, account_type=None, reg_limit=None, strict_limit=None, create_date=None, usage=None):  # noqa: E501
        """ReportageAccountInfoSchema - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._first_name = None
        self._last_name = None
        self._company = None
        self._account_type = None
        self._reg_limit = None
        self._strict_limit = None
        self._create_date = None
        self._usage = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if company is not None:
            self.company = company
        if account_type is not None:
            self.account_type = account_type
        if reg_limit is not None:
            self.reg_limit = reg_limit
        if strict_limit is not None:
            self.strict_limit = strict_limit
        if create_date is not None:
            self.create_date = create_date
        if usage is not None:
            self.usage = usage

    @property
    def email(self):
        """Gets the email of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The email of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ReportageAccountInfoSchema.

        :param email: The email of this ReportageAccountInfoSchema.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The first_name of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ReportageAccountInfoSchema.

        :param first_name: The first_name of this ReportageAccountInfoSchema.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The last_name of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ReportageAccountInfoSchema.

        :param last_name: The last_name of this ReportageAccountInfoSchema.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def company(self):
        """Gets the company of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The company of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ReportageAccountInfoSchema.

        :param company: The company of this ReportageAccountInfoSchema.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def account_type(self):
        """Gets the account_type of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The account_type of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this ReportageAccountInfoSchema.

        :param account_type: The account_type of this ReportageAccountInfoSchema.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def reg_limit(self):
        """Gets the reg_limit of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The reg_limit of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: int
        """
        return self._reg_limit

    @reg_limit.setter
    def reg_limit(self, reg_limit):
        """Sets the reg_limit of this ReportageAccountInfoSchema.

        :param reg_limit: The reg_limit of this ReportageAccountInfoSchema.  # noqa: E501
        :type: int
        """

        self._reg_limit = reg_limit

    @property
    def strict_limit(self):
        """Gets the strict_limit of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The strict_limit of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: bool
        """
        return self._strict_limit

    @strict_limit.setter
    def strict_limit(self, strict_limit):
        """Sets the strict_limit of this ReportageAccountInfoSchema.

        :param strict_limit: The strict_limit of this ReportageAccountInfoSchema.  # noqa: E501
        :type: bool
        """

        self._strict_limit = strict_limit

    @property
    def create_date(self):
        """Gets the create_date of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The create_date of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ReportageAccountInfoSchema.

        :param create_date: The create_date of this ReportageAccountInfoSchema.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def usage(self):
        """Gets the usage of this ReportageAccountInfoSchema.  # noqa: E501

        :return: The usage of this ReportageAccountInfoSchema.  # noqa: E501
        :rtype: ReportageAccountInfoUsageSchema
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ReportageAccountInfoSchema.

        :param usage: The usage of this ReportageAccountInfoSchema.  # noqa: E501
        :type: ReportageAccountInfoUsageSchema
        """

        self._usage = usage

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
        if issubclass(ReportageAccountInfoSchema, dict):
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
        if not isinstance(other, ReportageAccountInfoSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
