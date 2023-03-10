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


class AboutApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_about(self, **kwargs):  # noqa: E501
        """Get back the API version and Application name   # noqa: E501

        Get back the API version and application name.  The return value for this method will never change. This method largely exists for API parity with our on-premise or Managed Hosting products, which may return different release numbers from this endpoint.  For SCORM Cloud, this is effectively equal to the `/ping` resource.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_about(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AboutSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_about_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_about_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_about_with_http_info(self, **kwargs):  # noqa: E501
        """Get back the API version and Application name   # noqa: E501

        Get back the API version and application name.  The return value for this method will never change. This method largely exists for API parity with our on-premise or Managed Hosting products, which may return different release numbers from this endpoint.  For SCORM Cloud, this is effectively equal to the `/ping` resource.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_about_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AboutSchema
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
                    " to method get_about" % key
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
            '/about', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AboutSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
