# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import
from deprecated import deprecated

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rustici_software_cloud_v2.api_client import ApiClient


class ZoomiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_application_zoomi_keys(self, **kwargs):  # noqa: E501
        """Delete the Zoomi keys for an Application   # noqa: E501

        Deletes the Zoomi keys for an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application_zoomi_keys(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_application_zoomi_keys_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_application_zoomi_keys_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_application_zoomi_keys_with_http_info(self, **kwargs):  # noqa: E501
        """Delete the Zoomi keys for an Application   # noqa: E501

        Deletes the Zoomi keys for an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_application_zoomi_keys_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_application_zoomi_keys" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/key', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_zoomi_course(self, course_id, version_id, **kwargs):  # noqa: E501
        """Delete the Course from Zoomi   # noqa: E501

        Deletes the course from Zoomi, but the course will remain in SCORM Cloud.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_zoomi_course(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_zoomi_course_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_zoomi_course_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
            return data

    def delete_zoomi_course_with_http_info(self, course_id, version_id, **kwargs):  # noqa: E501
        """Delete the Course from Zoomi   # noqa: E501

        Deletes the course from Zoomi, but the course will remain in SCORM Cloud.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_zoomi_course_with_http_info(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'version_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_zoomi_course" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `delete_zoomi_course`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `delete_zoomi_course`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/course/{courseId}/version/{versionId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_application_zoomi_company_id(self, **kwargs):  # noqa: E501
        """Get the Zoomi company ID of an Application   # noqa: E501

        Returns the Zoomi company ID of an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_zoomi_company_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_zoomi_company_id_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_application_zoomi_company_id_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_application_zoomi_company_id_with_http_info(self, **kwargs):  # noqa: E501
        """Get the Zoomi company ID of an Application   # noqa: E501

        Returns the Zoomi company ID of an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_zoomi_company_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_application_zoomi_company_id" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StringResultSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_application_zoomi_public_key(self, **kwargs):  # noqa: E501
        """Get the Zoomi public key for an Application   # noqa: E501

        Returns the Zoomi public key for an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_zoomi_public_key(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_application_zoomi_public_key_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_application_zoomi_public_key_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_application_zoomi_public_key_with_http_info(self, **kwargs):  # noqa: E501
        """Get the Zoomi public key for an Application   # noqa: E501

        Returns the Zoomi public key for an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_application_zoomi_public_key_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_application_zoomi_public_key" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/key', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StringResultSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_course_zoomi_enabled(self, course_id, version_id, **kwargs):  # noqa: E501
        """Get the Zoomi enabled value of a Course Version   # noqa: E501

        Returns the Zoomi enabled value of a course version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_course_zoomi_enabled(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: EnabledSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_course_zoomi_enabled_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_course_zoomi_enabled_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
            return data

    def get_course_zoomi_enabled_with_http_info(self, course_id, version_id, **kwargs):  # noqa: E501
        """Get the Zoomi enabled value of a Course Version   # noqa: E501

        Returns the Zoomi enabled value of a course version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_course_zoomi_enabled_with_http_info(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: EnabledSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'version_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_course_zoomi_enabled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_course_zoomi_enabled`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_course_zoomi_enabled`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/course/{courseId}/version/{versionId}/enabled', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnabledSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zoomi_course_status(self, course_id, version_id, **kwargs):  # noqa: E501
        """Get the status for a Course from Zoomi   # noqa: E501

        Returns the status for a course and starts the upload process to Zoomi if not started.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zoomi_course_status(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_zoomi_course_status_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_zoomi_course_status_with_http_info(course_id, version_id, **kwargs)  # noqa: E501
            return data

    def get_zoomi_course_status_with_http_info(self, course_id, version_id, **kwargs):  # noqa: E501
        """Get the status for a Course from Zoomi   # noqa: E501

        Returns the status for a course and starts the upload process to Zoomi if not started.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_zoomi_course_status_with_http_info(course_id, version_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :return: StringResultSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'version_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zoomi_course_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `get_zoomi_course_status`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `get_zoomi_course_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/course/{courseId}/version/{versionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StringResultSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_course_version_to_zoomi(self, course_id, version_id, zoomi_course_options, **kwargs):  # noqa: E501
        """Begin the import process with Zoomi   # noqa: E501

        Begins the import process with Zoomi.  Must be followed up by a status call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_course_version_to_zoomi(course_id, version_id, zoomi_course_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :param ZoomiCourseOptionsSchema zoomi_course_options: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.import_course_version_to_zoomi_with_http_info(course_id, version_id, zoomi_course_options, **kwargs)  # noqa: E501
        else:
            (data) = self.import_course_version_to_zoomi_with_http_info(course_id, version_id, zoomi_course_options, **kwargs)  # noqa: E501
            return data

    def import_course_version_to_zoomi_with_http_info(self, course_id, version_id, zoomi_course_options, **kwargs):  # noqa: E501
        """Begin the import process with Zoomi   # noqa: E501

        Begins the import process with Zoomi.  Must be followed up by a status call.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_course_version_to_zoomi_with_http_info(course_id, version_id, zoomi_course_options, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :param ZoomiCourseOptionsSchema zoomi_course_options: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'version_id', 'zoomi_course_options']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method import_course_version_to_zoomi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `import_course_version_to_zoomi`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `import_course_version_to_zoomi`")  # noqa: E501
        # verify the required parameter 'zoomi_course_options' is set
        if ('zoomi_course_options' not in params or
                params['zoomi_course_options'] is None):
            raise ValueError("Missing the required parameter `zoomi_course_options` when calling `import_course_version_to_zoomi`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'zoomi_course_options' in params:
            body_params = params['zoomi_course_options']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/course/{courseId}/version/{versionId}/import', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_application_zoomi_company_id(self, zoomi_company_id, **kwargs):  # noqa: E501
        """Set the Zoomi company ID of an Application   # noqa: E501

        Sets the Zoomi company ID value of an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_application_zoomi_company_id(zoomi_company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ZoomiCompanyId zoomi_company_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_application_zoomi_company_id_with_http_info(zoomi_company_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_application_zoomi_company_id_with_http_info(zoomi_company_id, **kwargs)  # noqa: E501
            return data

    def set_application_zoomi_company_id_with_http_info(self, zoomi_company_id, **kwargs):  # noqa: E501
        """Set the Zoomi company ID of an Application   # noqa: E501

        Sets the Zoomi company ID value of an application.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_application_zoomi_company_id_with_http_info(zoomi_company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ZoomiCompanyId zoomi_company_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zoomi_company_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_application_zoomi_company_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zoomi_company_id' is set
        if ('zoomi_company_id' not in params or
                params['zoomi_company_id'] is None):
            raise ValueError("Missing the required parameter `zoomi_company_id` when calling `set_application_zoomi_company_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'zoomi_company_id' in params:
            body_params = params['zoomi_company_id']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_course_zoomi_enabled(self, course_id, version_id, enabled, **kwargs):  # noqa: E501
        """Set the Zoomi enabled value of a Course Version   # noqa: E501

        Sets the Zoomi enabled value of a course version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_course_zoomi_enabled(course_id, version_id, enabled, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :param EnabledSchema enabled: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_course_zoomi_enabled_with_http_info(course_id, version_id, enabled, **kwargs)  # noqa: E501
        else:
            (data) = self.set_course_zoomi_enabled_with_http_info(course_id, version_id, enabled, **kwargs)  # noqa: E501
            return data

    def set_course_zoomi_enabled_with_http_info(self, course_id, version_id, enabled, **kwargs):  # noqa: E501
        """Set the Zoomi enabled value of a Course Version   # noqa: E501

        Sets the Zoomi enabled value of a course version.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_course_zoomi_enabled_with_http_info(course_id, version_id, enabled, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str course_id: (required)
        :param int version_id: (required)
        :param EnabledSchema enabled: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['course_id', 'version_id', 'enabled']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_course_zoomi_enabled" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'course_id' is set
        if ('course_id' not in params or
                params['course_id'] is None):
            raise ValueError("Missing the required parameter `course_id` when calling `set_course_zoomi_enabled`")  # noqa: E501
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params or
                params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `set_course_zoomi_enabled`")  # noqa: E501
        # verify the required parameter 'enabled' is set
        if ('enabled' not in params or
                params['enabled'] is None):
            raise ValueError("Missing the required parameter `enabled` when calling `set_course_zoomi_enabled`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'course_id' in params:
            path_params['courseId'] = params['course_id']  # noqa: E501
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'enabled' in params:
            body_params = params['enabled']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/zoomi/course/{courseId}/version/{versionId}/enabled', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
