# !/usr/bin/env python
# coding=utf-8
"""
Samples for app blb client.
"""

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.services.blb.app_blb_client import AppBlbClient
from baidubce.exception import BceHttpClientError

if __name__ == "__main__":

    config = BceClientConfiguration(
        credentials=BceCredentials(
            access_key_id='your-ak',  # 用户的ak
            secret_access_key='your-sk'  # 用户的sk
        ),
        endpoint='host'  # 请求的域名信息

    )

    # create an app blb client
    app_blb_client = AppBlbClient(config)

    blb_id = "lb-a889d7d4"
    sg_id = "sg-8fdb32b1"
    port = "port-ba811b4f"
    health_check_down_retry = 5

    # update server group port
    try:
        app_blb_client.update_app_server_group_port(blb_id, sg_id, port,
                                                    health_check_down_retry=health_check_down_retry)
    except BceHttpClientError as e:
        print("Exception when calling api: %s\n" % e)
