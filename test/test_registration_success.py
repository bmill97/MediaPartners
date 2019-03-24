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

from __future__ import absolute_import

import os
import sys
import unittest

import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from rustici_software_cloud_v2.models.registration_success import RegistrationSuccess


class TestRegistrationSuccess(unittest.TestCase):
    """ RegistrationSuccess unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegistrationSuccess(self):
        """
        Test RegistrationSuccess
        """
        model = rustici_software_cloud_v2.models.registration_success.RegistrationSuccess()


if __name__ == '__main__':
    unittest.main()
