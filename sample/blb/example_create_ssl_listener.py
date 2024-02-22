# -*- coding: utf-8 -*-
# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with
# the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the
# specific language governing permissions and limitations under the License.
"""
Example for create blb ssl listener.
"""

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.exception import BceHttpClientError

from baidubce.services.blb import blb_client

if __name__ == '__main__':
    ak = "Your AK"  # 账号AK
    sk = "Your SK"  # 账号AK
    endpoint = 'Your Endpoint'  # 服务对应的Region域名
    config = BceClientConfiguration(credentials=BceCredentials(access_key_id=ak,
                                    secret_access_key=sk), endpoint=endpoint)
    blb_client = blb_client.BlbClient(config) # 初始化client
    try:
        blb_id = 'Your BlbId' # 指定的BLB ID
        listener_port = 'Your ListenerPort' # 监听器的监听端口
        backend_port = 'Your BackendPort' # 后端服务器的监听端口
        scheduler = 'Your Scheduler' # 负载均衡算法
        cert_ids = ["Your CertIds"] # 监听器要加载的证书链
        resp = blb_client.create_ssl_listener(blb_id=blb_id, listener_port=listener_port,
                                              backend_port=backend_port, scheduler=scheduler, cert_ids=cert_ids) # 创建ssl监听器
        print("[example] create blb ssl listener response : {}".format(resp))
    except BceHttpClientError as e:
        print("Exception when calling api: %s\n" % e)