# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0 beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class LaunchHistorySchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, instance=None, score=None, completion_status='UNKNOWN', success_status='UNKNOWN', history_log=None, total_seconds_tracked=None, launch_time=None, exit_time=None, last_runtime_update=None):
        """
        LaunchHistorySchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'instance': 'int',
            'score': 'ScoreSchema',
            'completion_status': 'str',
            'success_status': 'str',
            'history_log': 'str',
            'total_seconds_tracked': 'float',
            'launch_time': 'datetime',
            'exit_time': 'datetime',
            'last_runtime_update': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'instance': 'instance',
            'score': 'score',
            'completion_status': 'completionStatus',
            'success_status': 'successStatus',
            'history_log': 'historyLog',
            'total_seconds_tracked': 'totalSecondsTracked',
            'launch_time': 'launchTime',
            'exit_time': 'exitTime',
            'last_runtime_update': 'lastRuntimeUpdate'
        }

        self._id = id
        self._instance = instance
        self._score = score
        self._completion_status = completion_status
        self._success_status = success_status
        self._history_log = history_log
        self._total_seconds_tracked = total_seconds_tracked
        self._launch_time = launch_time
        self._exit_time = exit_time
        self._last_runtime_update = last_runtime_update

    @property
    def id(self):
        """
        Gets the id of this LaunchHistorySchema.


        :return: The id of this LaunchHistorySchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LaunchHistorySchema.


        :param id: The id of this LaunchHistorySchema.
        :type: str
        """

        self._id = id

    @property
    def instance(self):
        """
        Gets the instance of this LaunchHistorySchema.


        :return: The instance of this LaunchHistorySchema.
        :rtype: int
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """
        Sets the instance of this LaunchHistorySchema.


        :param instance: The instance of this LaunchHistorySchema.
        :type: int
        """

        self._instance = instance

    @property
    def score(self):
        """
        Gets the score of this LaunchHistorySchema.


        :return: The score of this LaunchHistorySchema.
        :rtype: ScoreSchema
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this LaunchHistorySchema.


        :param score: The score of this LaunchHistorySchema.
        :type: ScoreSchema
        """

        self._score = score

    @property
    def completion_status(self):
        """
        Gets the completion_status of this LaunchHistorySchema.


        :return: The completion_status of this LaunchHistorySchema.
        :rtype: str
        """
        return self._completion_status

    @completion_status.setter
    def completion_status(self, completion_status):
        """
        Sets the completion_status of this LaunchHistorySchema.


        :param completion_status: The completion_status of this LaunchHistorySchema.
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLETED", "INCOMPLETE"]
        if completion_status not in allowed_values:
            raise ValueError(
                "Invalid value for `completion_status` ({0}), must be one of {1}"
                .format(completion_status, allowed_values)
            )

        self._completion_status = completion_status

    @property
    def success_status(self):
        """
        Gets the success_status of this LaunchHistorySchema.


        :return: The success_status of this LaunchHistorySchema.
        :rtype: str
        """
        return self._success_status

    @success_status.setter
    def success_status(self, success_status):
        """
        Sets the success_status of this LaunchHistorySchema.


        :param success_status: The success_status of this LaunchHistorySchema.
        :type: str
        """
        allowed_values = ["UNKNOWN", "PASSED", "FAILED"]
        if success_status not in allowed_values:
            raise ValueError(
                "Invalid value for `success_status` ({0}), must be one of {1}"
                .format(success_status, allowed_values)
            )

        self._success_status = success_status

    @property
    def history_log(self):
        """
        Gets the history_log of this LaunchHistorySchema.


        :return: The history_log of this LaunchHistorySchema.
        :rtype: str
        """
        return self._history_log

    @history_log.setter
    def history_log(self, history_log):
        """
        Sets the history_log of this LaunchHistorySchema.


        :param history_log: The history_log of this LaunchHistorySchema.
        :type: str
        """

        self._history_log = history_log

    @property
    def total_seconds_tracked(self):
        """
        Gets the total_seconds_tracked of this LaunchHistorySchema.


        :return: The total_seconds_tracked of this LaunchHistorySchema.
        :rtype: float
        """
        return self._total_seconds_tracked

    @total_seconds_tracked.setter
    def total_seconds_tracked(self, total_seconds_tracked):
        """
        Sets the total_seconds_tracked of this LaunchHistorySchema.


        :param total_seconds_tracked: The total_seconds_tracked of this LaunchHistorySchema.
        :type: float
        """

        self._total_seconds_tracked = total_seconds_tracked

    @property
    def launch_time(self):
        """
        Gets the launch_time of this LaunchHistorySchema.
        The time of the launch in UTC

        :return: The launch_time of this LaunchHistorySchema.
        :rtype: datetime
        """
        return self._launch_time

    @launch_time.setter
    def launch_time(self, launch_time):
        """
        Sets the launch_time of this LaunchHistorySchema.
        The time of the launch in UTC

        :param launch_time: The launch_time of this LaunchHistorySchema.
        :type: datetime
        """

        self._launch_time = launch_time

    @property
    def exit_time(self):
        """
        Gets the exit_time of this LaunchHistorySchema.
        The time of the exit in UTC

        :return: The exit_time of this LaunchHistorySchema.
        :rtype: datetime
        """
        return self._exit_time

    @exit_time.setter
    def exit_time(self, exit_time):
        """
        Sets the exit_time of this LaunchHistorySchema.
        The time of the exit in UTC

        :param exit_time: The exit_time of this LaunchHistorySchema.
        :type: datetime
        """

        self._exit_time = exit_time

    @property
    def last_runtime_update(self):
        """
        Gets the last_runtime_update of this LaunchHistorySchema.
        The time of the last runtime update in UTC

        :return: The last_runtime_update of this LaunchHistorySchema.
        :rtype: datetime
        """
        return self._last_runtime_update

    @last_runtime_update.setter
    def last_runtime_update(self, last_runtime_update):
        """
        Sets the last_runtime_update of this LaunchHistorySchema.
        The time of the last runtime update in UTC

        :param last_runtime_update: The last_runtime_update of this LaunchHistorySchema.
        :type: datetime
        """

        self._last_runtime_update = last_runtime_update

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
