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


class RegistrationSchema(object):
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
        'instance': 'int',
        'xapi_registration_id': 'str',
        'dispatch_id': 'str',
        'updated': 'datetime',
        'registration_completion': 'RegistrationCompletion',
        'registration_completion_amount': 'float',
        'registration_success': 'RegistrationSuccess',
        'score': 'ScoreSchema',
        'total_seconds_tracked': 'float',
        'first_access_date': 'datetime',
        'last_access_date': 'datetime',
        'completed_date': 'datetime',
        'created_date': 'datetime',
        'course': 'CourseReferenceSchema',
        'learner': 'LearnerSchema',
        'tags': 'list[str]',
        'global_objectives': 'list[ObjectiveSchema]',
        'shared_data': 'list[SharedDataEntrySchema]',
        'suspended_activity_id': 'str',
        'activity_details': 'ActivityResultSchema'
    }

    attribute_map = {
        'id': 'id',
        'instance': 'instance',
        'xapi_registration_id': 'xapiRegistrationId',
        'dispatch_id': 'dispatchId',
        'updated': 'updated',
        'registration_completion': 'registrationCompletion',
        'registration_completion_amount': 'registrationCompletionAmount',
        'registration_success': 'registrationSuccess',
        'score': 'score',
        'total_seconds_tracked': 'totalSecondsTracked',
        'first_access_date': 'firstAccessDate',
        'last_access_date': 'lastAccessDate',
        'completed_date': 'completedDate',
        'created_date': 'createdDate',
        'course': 'course',
        'learner': 'learner',
        'tags': 'tags',
        'global_objectives': 'globalObjectives',
        'shared_data': 'sharedData',
        'suspended_activity_id': 'suspendedActivityId',
        'activity_details': 'activityDetails'
    }

    def __init__(self, id=None, instance=None, xapi_registration_id=None, dispatch_id=None, updated=None, registration_completion=None, registration_completion_amount=None, registration_success=None, score=None, total_seconds_tracked=None, first_access_date=None, last_access_date=None, completed_date=None, created_date=None, course=None, learner=None, tags=None, global_objectives=None, shared_data=None, suspended_activity_id=None, activity_details=None):  # noqa: E501
        """RegistrationSchema - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._instance = None
        self._xapi_registration_id = None
        self._dispatch_id = None
        self._updated = None
        self._registration_completion = None
        self._registration_completion_amount = None
        self._registration_success = None
        self._score = None
        self._total_seconds_tracked = None
        self._first_access_date = None
        self._last_access_date = None
        self._completed_date = None
        self._created_date = None
        self._course = None
        self._learner = None
        self._tags = None
        self._global_objectives = None
        self._shared_data = None
        self._suspended_activity_id = None
        self._activity_details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance is not None:
            self.instance = instance
        if xapi_registration_id is not None:
            self.xapi_registration_id = xapi_registration_id
        if dispatch_id is not None:
            self.dispatch_id = dispatch_id
        if updated is not None:
            self.updated = updated
        if registration_completion is not None:
            self.registration_completion = registration_completion
        if registration_completion_amount is not None:
            self.registration_completion_amount = registration_completion_amount
        if registration_success is not None:
            self.registration_success = registration_success
        if score is not None:
            self.score = score
        if total_seconds_tracked is not None:
            self.total_seconds_tracked = total_seconds_tracked
        if first_access_date is not None:
            self.first_access_date = first_access_date
        if last_access_date is not None:
            self.last_access_date = last_access_date
        if completed_date is not None:
            self.completed_date = completed_date
        if created_date is not None:
            self.created_date = created_date
        if course is not None:
            self.course = course
        if learner is not None:
            self.learner = learner
        if tags is not None:
            self.tags = tags
        if global_objectives is not None:
            self.global_objectives = global_objectives
        if shared_data is not None:
            self.shared_data = shared_data
        if suspended_activity_id is not None:
            self.suspended_activity_id = suspended_activity_id
        if activity_details is not None:
            self.activity_details = activity_details

    @property
    def id(self):
        """Gets the id of this RegistrationSchema.  # noqa: E501

        :return: The id of this RegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegistrationSchema.

        :param id: The id of this RegistrationSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def instance(self):
        """Gets the instance of this RegistrationSchema.  # noqa: E501

        :return: The instance of this RegistrationSchema.  # noqa: E501
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this RegistrationSchema.

        :param instance: The instance of this RegistrationSchema.  # noqa: E501
        :type: int
        """

        self._instance = instance

    @property
    def xapi_registration_id(self):
        """Gets the xapi_registration_id of this RegistrationSchema.  # noqa: E501

        xAPI registration id associated with this registration  # noqa: E501

        :return: The xapi_registration_id of this RegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._xapi_registration_id

    @xapi_registration_id.setter
    def xapi_registration_id(self, xapi_registration_id):
        """Sets the xapi_registration_id of this RegistrationSchema.

        xAPI registration id associated with this registration  # noqa: E501

        :param xapi_registration_id: The xapi_registration_id of this RegistrationSchema.  # noqa: E501
        :type: str
        """

        self._xapi_registration_id = xapi_registration_id

    @property
    def dispatch_id(self):
        """Gets the dispatch_id of this RegistrationSchema.  # noqa: E501

        Dispatch ID for this registration, if applicable  # noqa: E501

        :return: The dispatch_id of this RegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._dispatch_id

    @dispatch_id.setter
    def dispatch_id(self, dispatch_id):
        """Sets the dispatch_id of this RegistrationSchema.

        Dispatch ID for this registration, if applicable  # noqa: E501

        :param dispatch_id: The dispatch_id of this RegistrationSchema.  # noqa: E501
        :type: str
        """

        self._dispatch_id = dispatch_id

    @property
    def updated(self):
        """Gets the updated of this RegistrationSchema.  # noqa: E501

        :return: The updated of this RegistrationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RegistrationSchema.

        :param updated: The updated of this RegistrationSchema.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def registration_completion(self):
        """Gets the registration_completion of this RegistrationSchema.  # noqa: E501

        :return: The registration_completion of this RegistrationSchema.  # noqa: E501
        :rtype: RegistrationCompletion
        """
        return self._registration_completion

    @registration_completion.setter
    def registration_completion(self, registration_completion):
        """Sets the registration_completion of this RegistrationSchema.

        :param registration_completion: The registration_completion of this RegistrationSchema.  # noqa: E501
        :type: RegistrationCompletion
        """

        self._registration_completion = registration_completion

    @property
    def registration_completion_amount(self):
        """Gets the registration_completion_amount of this RegistrationSchema.  # noqa: E501

        :return: The registration_completion_amount of this RegistrationSchema.  # noqa: E501
        :rtype: float
        """
        return self._registration_completion_amount

    @registration_completion_amount.setter
    def registration_completion_amount(self, registration_completion_amount):
        """Sets the registration_completion_amount of this RegistrationSchema.

        :param registration_completion_amount: The registration_completion_amount of this RegistrationSchema.  # noqa: E501
        :type: float
        """

        self._registration_completion_amount = registration_completion_amount

    @property
    def registration_success(self):
        """Gets the registration_success of this RegistrationSchema.  # noqa: E501

        :return: The registration_success of this RegistrationSchema.  # noqa: E501
        :rtype: RegistrationSuccess
        """
        return self._registration_success

    @registration_success.setter
    def registration_success(self, registration_success):
        """Sets the registration_success of this RegistrationSchema.

        :param registration_success: The registration_success of this RegistrationSchema.  # noqa: E501
        :type: RegistrationSuccess
        """

        self._registration_success = registration_success

    @property
    def score(self):
        """Gets the score of this RegistrationSchema.  # noqa: E501

        :return: The score of this RegistrationSchema.  # noqa: E501
        :rtype: ScoreSchema
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RegistrationSchema.

        :param score: The score of this RegistrationSchema.  # noqa: E501
        :type: ScoreSchema
        """

        self._score = score

    @property
    def total_seconds_tracked(self):
        """Gets the total_seconds_tracked of this RegistrationSchema.  # noqa: E501

        :return: The total_seconds_tracked of this RegistrationSchema.  # noqa: E501
        :rtype: float
        """
        return self._total_seconds_tracked

    @total_seconds_tracked.setter
    def total_seconds_tracked(self, total_seconds_tracked):
        """Sets the total_seconds_tracked of this RegistrationSchema.

        :param total_seconds_tracked: The total_seconds_tracked of this RegistrationSchema.  # noqa: E501
        :type: float
        """

        self._total_seconds_tracked = total_seconds_tracked

    @property
    def first_access_date(self):
        """Gets the first_access_date of this RegistrationSchema.  # noqa: E501

        :return: The first_access_date of this RegistrationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._first_access_date

    @first_access_date.setter
    def first_access_date(self, first_access_date):
        """Sets the first_access_date of this RegistrationSchema.

        :param first_access_date: The first_access_date of this RegistrationSchema.  # noqa: E501
        :type: datetime
        """

        self._first_access_date = first_access_date

    @property
    def last_access_date(self):
        """Gets the last_access_date of this RegistrationSchema.  # noqa: E501

        :return: The last_access_date of this RegistrationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._last_access_date

    @last_access_date.setter
    def last_access_date(self, last_access_date):
        """Sets the last_access_date of this RegistrationSchema.

        :param last_access_date: The last_access_date of this RegistrationSchema.  # noqa: E501
        :type: datetime
        """

        self._last_access_date = last_access_date

    @property
    def completed_date(self):
        """Gets the completed_date of this RegistrationSchema.  # noqa: E501

        :return: The completed_date of this RegistrationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_date

    @completed_date.setter
    def completed_date(self, completed_date):
        """Sets the completed_date of this RegistrationSchema.

        :param completed_date: The completed_date of this RegistrationSchema.  # noqa: E501
        :type: datetime
        """

        self._completed_date = completed_date

    @property
    def created_date(self):
        """Gets the created_date of this RegistrationSchema.  # noqa: E501

        :return: The created_date of this RegistrationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RegistrationSchema.

        :param created_date: The created_date of this RegistrationSchema.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def course(self):
        """Gets the course of this RegistrationSchema.  # noqa: E501

        :return: The course of this RegistrationSchema.  # noqa: E501
        :rtype: CourseReferenceSchema
        """
        return self._course

    @course.setter
    def course(self, course):
        """Sets the course of this RegistrationSchema.

        :param course: The course of this RegistrationSchema.  # noqa: E501
        :type: CourseReferenceSchema
        """

        self._course = course

    @property
    def learner(self):
        """Gets the learner of this RegistrationSchema.  # noqa: E501

        :return: The learner of this RegistrationSchema.  # noqa: E501
        :rtype: LearnerSchema
        """
        return self._learner

    @learner.setter
    def learner(self, learner):
        """Sets the learner of this RegistrationSchema.

        :param learner: The learner of this RegistrationSchema.  # noqa: E501
        :type: LearnerSchema
        """

        self._learner = learner

    @property
    def tags(self):
        """Gets the tags of this RegistrationSchema.  # noqa: E501

        :return: The tags of this RegistrationSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RegistrationSchema.

        :param tags: The tags of this RegistrationSchema.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def global_objectives(self):
        """Gets the global_objectives of this RegistrationSchema.  # noqa: E501

        :return: The global_objectives of this RegistrationSchema.  # noqa: E501
        :rtype: list[ObjectiveSchema]
        """
        return self._global_objectives

    @global_objectives.setter
    def global_objectives(self, global_objectives):
        """Sets the global_objectives of this RegistrationSchema.

        :param global_objectives: The global_objectives of this RegistrationSchema.  # noqa: E501
        :type: list[ObjectiveSchema]
        """

        self._global_objectives = global_objectives

    @property
    def shared_data(self):
        """Gets the shared_data of this RegistrationSchema.  # noqa: E501

        :return: The shared_data of this RegistrationSchema.  # noqa: E501
        :rtype: list[SharedDataEntrySchema]
        """
        return self._shared_data

    @shared_data.setter
    def shared_data(self, shared_data):
        """Sets the shared_data of this RegistrationSchema.

        :param shared_data: The shared_data of this RegistrationSchema.  # noqa: E501
        :type: list[SharedDataEntrySchema]
        """

        self._shared_data = shared_data

    @property
    def suspended_activity_id(self):
        """Gets the suspended_activity_id of this RegistrationSchema.  # noqa: E501

        :return: The suspended_activity_id of this RegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._suspended_activity_id

    @suspended_activity_id.setter
    def suspended_activity_id(self, suspended_activity_id):
        """Sets the suspended_activity_id of this RegistrationSchema.

        :param suspended_activity_id: The suspended_activity_id of this RegistrationSchema.  # noqa: E501
        :type: str
        """

        self._suspended_activity_id = suspended_activity_id

    @property
    def activity_details(self):
        """Gets the activity_details of this RegistrationSchema.  # noqa: E501

        :return: The activity_details of this RegistrationSchema.  # noqa: E501
        :rtype: ActivityResultSchema
        """
        return self._activity_details

    @activity_details.setter
    def activity_details(self, activity_details):
        """Sets the activity_details of this RegistrationSchema.

        :param activity_details: The activity_details of this RegistrationSchema.  # noqa: E501
        :type: ActivityResultSchema
        """

        self._activity_details = activity_details

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
        if issubclass(RegistrationSchema, dict):
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
        if not isinstance(other, RegistrationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
