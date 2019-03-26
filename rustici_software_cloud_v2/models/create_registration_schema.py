# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0 beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rustici_software_cloud_v2.models.learner_schema import LearnerSchema  # noqa: F401,E501
from rustici_software_cloud_v2.models.post_back_schema import PostBackSchema  # noqa: F401,E501
from rustici_software_cloud_v2.models.registration_schema import RegistrationSchema  # noqa: F401,E501
from rustici_software_cloud_v2.models.settings_post_schema import SettingsPostSchema  # noqa: F401,E501


class CreateRegistrationSchema(object):
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
        'course_id': 'str',
        'learner': 'LearnerSchema',
        'registration_id': 'str',
        'xapi_registration_id': 'str',
        'learner_tags': 'list[str]',
        'course_tags': 'list[str]',
        'registration_tags': 'list[str]',
        'post_back': 'PostBackSchema',
        'initial_registration_state': 'RegistrationSchema',
        'initial_settings': 'SettingsPostSchema'
    }

    attribute_map = {
        'course_id': 'courseId',
        'learner': 'learner',
        'registration_id': 'registrationId',
        'xapi_registration_id': 'xapiRegistrationId',
        'learner_tags': 'learnerTags',
        'course_tags': 'courseTags',
        'registration_tags': 'registrationTags',
        'post_back': 'postBack',
        'initial_registration_state': 'initialRegistrationState',
        'initial_settings': 'initialSettings'
    }

    def __init__(self, course_id=None, learner=None, registration_id=None, xapi_registration_id=None, learner_tags=None, course_tags=None, registration_tags=None, post_back=None, initial_registration_state=None, initial_settings=None):  # noqa: E501
        """CreateRegistrationSchema - a model defined in Swagger"""  # noqa: E501

        self._course_id = None
        self._learner = None
        self._registration_id = None
        self._xapi_registration_id = None
        self._learner_tags = None
        self._course_tags = None
        self._registration_tags = None
        self._post_back = None
        self._initial_registration_state = None
        self._initial_settings = None
        self.discriminator = None

        self.course_id = course_id
        self.learner = learner
        self.registration_id = registration_id
        if xapi_registration_id is not None:
            self.xapi_registration_id = xapi_registration_id
        if learner_tags is not None:
            self.learner_tags = learner_tags
        if course_tags is not None:
            self.course_tags = course_tags
        if registration_tags is not None:
            self.registration_tags = registration_tags
        if post_back is not None:
            self.post_back = post_back
        if initial_registration_state is not None:
            self.initial_registration_state = initial_registration_state
        if initial_settings is not None:
            self.initial_settings = initial_settings

    @property
    def course_id(self):
        """Gets the course_id of this CreateRegistrationSchema.  # noqa: E501


        :return: The course_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """Sets the course_id of this CreateRegistrationSchema.


        :param course_id: The course_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """
        if course_id is None:
            raise ValueError("Invalid value for `course_id`, must not be `None`")  # noqa: E501

        self._course_id = course_id

    @property
    def learner(self):
        """Gets the learner of this CreateRegistrationSchema.  # noqa: E501


        :return: The learner of this CreateRegistrationSchema.  # noqa: E501
        :rtype: LearnerSchema
        """
        return self._learner

    @learner.setter
    def learner(self, learner):
        """Sets the learner of this CreateRegistrationSchema.


        :param learner: The learner of this CreateRegistrationSchema.  # noqa: E501
        :type: LearnerSchema
        """
        if learner is None:
            raise ValueError("Invalid value for `learner`, must not be `None`")  # noqa: E501

        self._learner = learner

    @property
    def registration_id(self):
        """Gets the registration_id of this CreateRegistrationSchema.  # noqa: E501


        :return: The registration_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this CreateRegistrationSchema.


        :param registration_id: The registration_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """
        if registration_id is None:
            raise ValueError("Invalid value for `registration_id`, must not be `None`")  # noqa: E501

        self._registration_id = registration_id

    @property
    def xapi_registration_id(self):
        """Gets the xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501

        The xapiRegistrationId to be associated with this registration. If not specified, the system will assign an xapiRegistrationId. As per the xApi specification, this must be a UUID.  # noqa: E501

        :return: The xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._xapi_registration_id

    @xapi_registration_id.setter
    def xapi_registration_id(self, xapi_registration_id):
        """Sets the xapi_registration_id of this CreateRegistrationSchema.

        The xapiRegistrationId to be associated with this registration. If not specified, the system will assign an xapiRegistrationId. As per the xApi specification, this must be a UUID.  # noqa: E501

        :param xapi_registration_id: The xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """

        self._xapi_registration_id = xapi_registration_id

    @property
    def learner_tags(self):
        """Gets the learner_tags of this CreateRegistrationSchema.  # noqa: E501


        :return: The learner_tags of this CreateRegistrationSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._learner_tags

    @learner_tags.setter
    def learner_tags(self, learner_tags):
        """Sets the learner_tags of this CreateRegistrationSchema.


        :param learner_tags: The learner_tags of this CreateRegistrationSchema.  # noqa: E501
        :type: list[str]
        """

        self._learner_tags = learner_tags

    @property
    def course_tags(self):
        """Gets the course_tags of this CreateRegistrationSchema.  # noqa: E501


        :return: The course_tags of this CreateRegistrationSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._course_tags

    @course_tags.setter
    def course_tags(self, course_tags):
        """Sets the course_tags of this CreateRegistrationSchema.


        :param course_tags: The course_tags of this CreateRegistrationSchema.  # noqa: E501
        :type: list[str]
        """

        self._course_tags = course_tags

    @property
    def registration_tags(self):
        """Gets the registration_tags of this CreateRegistrationSchema.  # noqa: E501


        :return: The registration_tags of this CreateRegistrationSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._registration_tags

    @registration_tags.setter
    def registration_tags(self, registration_tags):
        """Sets the registration_tags of this CreateRegistrationSchema.


        :param registration_tags: The registration_tags of this CreateRegistrationSchema.  # noqa: E501
        :type: list[str]
        """

        self._registration_tags = registration_tags

    @property
    def post_back(self):
        """Gets the post_back of this CreateRegistrationSchema.  # noqa: E501

        Specifies an optional override URL for which to post activity and status data in real time as the course is completed. By default all of these settings are read from your configuration.  # noqa: E501

        :return: The post_back of this CreateRegistrationSchema.  # noqa: E501
        :rtype: PostBackSchema
        """
        return self._post_back

    @post_back.setter
    def post_back(self, post_back):
        """Sets the post_back of this CreateRegistrationSchema.

        Specifies an optional override URL for which to post activity and status data in real time as the course is completed. By default all of these settings are read from your configuration.  # noqa: E501

        :param post_back: The post_back of this CreateRegistrationSchema.  # noqa: E501
        :type: PostBackSchema
        """

        self._post_back = post_back

    @property
    def initial_registration_state(self):
        """Gets the initial_registration_state of this CreateRegistrationSchema.  # noqa: E501


        :return: The initial_registration_state of this CreateRegistrationSchema.  # noqa: E501
        :rtype: RegistrationSchema
        """
        return self._initial_registration_state

    @initial_registration_state.setter
    def initial_registration_state(self, initial_registration_state):
        """Sets the initial_registration_state of this CreateRegistrationSchema.


        :param initial_registration_state: The initial_registration_state of this CreateRegistrationSchema.  # noqa: E501
        :type: RegistrationSchema
        """

        self._initial_registration_state = initial_registration_state

    @property
    def initial_settings(self):
        """Gets the initial_settings of this CreateRegistrationSchema.  # noqa: E501


        :return: The initial_settings of this CreateRegistrationSchema.  # noqa: E501
        :rtype: SettingsPostSchema
        """
        return self._initial_settings

    @initial_settings.setter
    def initial_settings(self, initial_settings):
        """Sets the initial_settings of this CreateRegistrationSchema.


        :param initial_settings: The initial_settings of this CreateRegistrationSchema.  # noqa: E501
        :type: SettingsPostSchema
        """

        self._initial_settings = initial_settings

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
        if issubclass(CreateRegistrationSchema, dict):
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
        if not isinstance(other, CreateRegistrationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other