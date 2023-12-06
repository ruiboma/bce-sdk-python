# -*- coding: utf-8 -*-

# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
#  of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions
# and limitations under the License.
"""
This module provides a client class for ENI.
"""

import copy
import json
import logging
import uuid

from baidubce import bce_base_client
from baidubce.auth import bce_v1_signer
from baidubce.http import bce_http_client
from baidubce.http import handler
from baidubce.http import http_methods

from baidubce.utils import required
from baidubce import compat

_logger = logging.getLogger(__name__)


class EniClient(bce_base_client.BceBaseClient):
    """
    ENI base sdk client
    """

    prefix = b'/v1'

    def __init__(self, config=None):
        bce_base_client.BceBaseClient.__init__(self, config)

    def _merge_config(self, config=None):
        """
        :param config:
        :type config: baidubce.BceClientConfiguration
        :return:
        """
        if config is None:
            return self.config
        else:
            new_config = copy.copy(self.config)
            new_config.merge_non_none_values(config)
            return new_config

    def _send_request(self, http_method, path,
                      body=None, headers=None, params=None,
                      config=None, body_parser=None):
        config = self._merge_config(config)
        if body_parser is None:
            body_parser = handler.parse_json
        if headers is None:
            headers = {b'Accept': b'*/*', b'Content-Type': b'application/json;charset=utf-8'}
        return bce_http_client.send_request(
            config, bce_v1_signer.sign, [handler.parse_error, body_parser],
            http_method, EniClient.prefix + path, body, headers, params)

    @required(name=(bytes, str), subnet_id=(bytes, str), security_group_ids=list, 
              enterprise_security_group_ids=list, eni_ip_address_list=list, eni_ipv6_address_list=list)
    def create_eni(self, name, subnet_id, security_group_ids=None, enterprise_security_group_ids=None,
                   eni_ip_address_list=None, eni_ipv6_address_list=None, description=None, 
                   client_token=None, config=None):
        """
        :param name:
            The name of eni to be created.
        :type name: string

        :param subnet_id:
            The parameter to specify the id of subnet from vpc
        :type subnet_id: string

        :param security_group_ids:
            security_group_ids
        :type security_group_ids: list<string>

        :param enterprise_security_group_ids:
            enterprise_security_group_ids
        :type enterprise_security_group_ids: list<string>

        :param eni_ip_address_list:
            The parameter to specify the ipv4 address list of eni
        :type eni_ip_address_list: eni_model.EniIPSet

        :param eni_ipv6_address_list:
            The parameter to specify the ipv6 address list of eni
        :type eni_ip_address_list: eni_model.EniIPSet

        :param description:
            The description of the eni.
        :type description: string

        :param client_token:
            An ASCII string whose length is less than 64.
            The request will be idempotent if clientToken is provided.
            If the clientToken is not specified by the user, a random String generated by default algorithm will be used.
        :type client_token: string

        :param config:
        :type config: baidubce.BceClientConfiguration

        :return:
        :rtype baidubce.bce_response.BceResponse
        """
        path = b'/eni'
        params = {}
        if client_token is None:
            params[b'clientToken'] = generate_client_token()
        else:
            params[b'clientToken'] = client_token

        body = {
            'name': compat.convert_to_string(name),
            'subnetId': compat.convert_to_string(subnet_id),
        }
        if security_group_ids is not None:
            body['securityGroupIds'] = security_group_ids
        if enterprise_security_group_ids is not None:
            body['enterpriseSecurityGroupIds'] = enterprise_security_group_ids
        if eni_ip_address_list is not None:
            pri_ip_set = []
            for ip_set in eni_ip_address_list:
                pri_ip_set.append({"publicIpAddress":ip_set.public_ip, "primary":ip_set.primary,
                                  "privateIpAddress":ip_set.private_ip})
            body['privateIpSet'] = pri_ip_set
        if eni_ipv6_address_list is not None:
            pri_ipv6_set = []
            for ip_set in eni_ipv6_address_list:
                pri_ipv6_set.append({"publicIpAddress":ip_set.public_ip, "primary":ip_set.primary,
                                    "privateIpAddress":ip_set.private_ip})
            body['ipv6PrivateIpSet'] = pri_ipv6_set
        if description is not None:
            body['description'] = compat.convert_to_string(description)

        return self._send_request(http_methods.POST, path, body=json.dumps(body), params=params,
                                  config=config)
    
    @required(eni_id=(bytes, str))
    def delete_eni(self, eni_id, client_token=None, config=None):
        """
        release the eni(delete operation)
        if the eni has been bound, must unbind before releasing.

        :type eni_id: string
        :param eni_id: eni to be released

        :type client_token: string
        :param client_token: if the clientToken is not specified by the user,
         a random String generated by default algorithm will be used.

        :type config: baidubce.BceClientConfiguration
        :param config:

        :return: BceResponse
        """
        path = b'/eni/%s' % compat.convert_to_bytes(eni_id)
        if client_token is None:
            client_token = generate_client_token()
        params = {
            b'clientToken': client_token
        }
        return self._send_request(http_methods.DELETE, path, params=params,
                                  config=config)

def generate_client_token_by_uuid():
    """
    The default method to generate the random string for client_token
    if the optional parameter client_token is not specified by the user.

    :return:
    :rtype string
    """
    return str(uuid.uuid4())

generate_client_token = generate_client_token_by_uuid
