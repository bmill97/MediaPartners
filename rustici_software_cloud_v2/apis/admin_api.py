# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AdminApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_invitation_tags(self, invitation_id, tags, **kwargs):
        """
        Delete tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_invitation_tags(invitation_id, tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_invitation_tags_with_http_info(invitation_id, tags, **kwargs)
        else:
            (data) = self.delete_invitation_tags_with_http_info(invitation_id, tags, **kwargs)
            return data

    def delete_invitation_tags_with_http_info(self, invitation_id, tags, **kwargs):
        """
        Delete tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_invitation_tags_with_http_info(invitation_id, tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invitation_id', 'tags']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_invitation_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invitation_id' is set
        if ('invitation_id' not in params) or (params['invitation_id'] is None):
            raise ValueError("Missing the required parameter `invitation_id` when calling `delete_invitation_tags`")
        # verify the required parameter 'tags' is set
        if ('tags' not in params) or (params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `delete_invitation_tags`")


        collection_formats = {}

        resource_path = '/invitations/{invitationId}/tags'.replace('{format}', 'json')
        path_params = {}
        if 'invitation_id' in params:
            path_params['invitationId'] = params['invitation_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tags' in params:
            body_params = params['tags']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_invitation_tags(self, invitation_id, **kwargs):
        """
        Get the tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invitation_tags(invitation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :return: TagListSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_invitation_tags_with_http_info(invitation_id, **kwargs)
        else:
            (data) = self.get_invitation_tags_with_http_info(invitation_id, **kwargs)
            return data

    def get_invitation_tags_with_http_info(self, invitation_id, **kwargs):
        """
        Get the tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invitation_tags_with_http_info(invitation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :return: TagListSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invitation_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invitation_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invitation_id' is set
        if ('invitation_id' not in params) or (params['invitation_id'] is None):
            raise ValueError("Missing the required parameter `invitation_id` when calling `get_invitation_tags`")


        collection_formats = {}

        resource_path = '/invitations/{invitationId}/tags'.replace('{format}', 'json')
        path_params = {}
        if 'invitation_id' in params:
            path_params['invitationId'] = params['invitation_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TagListSchema',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_invitation_tags(self, invitation_id, tags, **kwargs):
        """
        Set the tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_invitation_tags(invitation_id, tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_invitation_tags_with_http_info(invitation_id, tags, **kwargs)
        else:
            (data) = self.put_invitation_tags_with_http_info(invitation_id, tags, **kwargs)
            return data

    def put_invitation_tags_with_http_info(self, invitation_id, tags, **kwargs):
        """
        Set the tags for this invitation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_invitation_tags_with_http_info(invitation_id, tags, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str invitation_id: invitation id (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invitation_id', 'tags']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_invitation_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invitation_id' is set
        if ('invitation_id' not in params) or (params['invitation_id'] is None):
            raise ValueError("Missing the required parameter `invitation_id` when calling `put_invitation_tags`")
        # verify the required parameter 'tags' is set
        if ('tags' not in params) or (params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `put_invitation_tags`")


        collection_formats = {}

        resource_path = '/invitations/{invitationId}/tags'.replace('{format}', 'json')
        path_params = {}
        if 'invitation_id' in params:
            path_params['invitationId'] = params['invitation_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tags' in params:
            body_params = params['tags']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def put_invitation_tags_batch(self, batch, **kwargs):
        """
        Sets all of the provided tags on all of the provided invitations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_invitation_tags_batch(batch, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BatchTagsSchema batch: Object representing an array of ids to apply an array of tags to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.put_invitation_tags_batch_with_http_info(batch, **kwargs)
        else:
            (data) = self.put_invitation_tags_batch_with_http_info(batch, **kwargs)
            return data

    def put_invitation_tags_batch_with_http_info(self, batch, **kwargs):
        """
        Sets all of the provided tags on all of the provided invitations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.put_invitation_tags_batch_with_http_info(batch, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BatchTagsSchema batch: Object representing an array of ids to apply an array of tags to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_invitation_tags_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch' is set
        if ('batch' not in params) or (params['batch'] is None):
            raise ValueError("Missing the required parameter `batch` when calling `put_invitation_tags_batch`")


        collection_formats = {}

        resource_path = '/invitations/tags'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch' in params:
            body_params = params['batch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)