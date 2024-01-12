# -*- coding: utf-8 -*-
# !/usr/bin/env python

# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"""
Samples for lbdc client.
"""

import lbdc_sample_conf as sample_conf
from baidubce.services.lbdc.lbdc_client import LbdcClient
from baidubce import exception


def test_list_lbdc_blb(lbdc_client, lbdc_id):
    """
    Query the list of blb instance in lbdc

    Args:
        :type lbdc_client: LbdcClient
        :param lbdc_client: lbdc sdk client

        :type lbdc_id: str
        :param lbdc_id: id of lbdc to query

    Return:
        None

    Raise:
        BceHttpClientError: http request error
    """
    try:
        response = lbdc_client.list_lbdc_blb(lbdc_id=lbdc_id)
        print(response)
    except exception.BceHttpClientError as e:
        # 异常处理
        print(e.last_error)
        print(e.request_id)
        print(e.code)
        return None


if __name__ == '__main__':
    # 初始化LbdcClient
    lbdc_client = LbdcClient(sample_conf.config)
    # lbdc的集群ID
    lbdc_id = b'lbdc-xxx'
    # 查询lbdc集群关联blb实例列表
    test_list_lbdc_blb(lbdc_client, lbdc_id)
