# !/usr/bin/env python
# coding=utf-8
"""
Samples for ipv6gateway client.
"""
import uuid

from baidubce import exception
from baidubce.services.ipv6gateway.ipv6gateway_client import IPv6GatewayClient
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials


def test_resize_ipv6_gateway(ipv6gateway_client, gateway_id, bandwidthInMbps):
    """
    resize ipv6 gateway.

    :param gateway_id:
        the ID of the ipv6 gateway.
    :type gateway_id: string

    :param bandwidthInMbps:
        bandwidth of the ipv6 gateway.
    :type bandwidthInMbps: int

    :return:
    :rtype baidubce.bce_response.BceResponse

    Raise:
        BceHttpClientError: http request error
    """
    try:
        res = ipv6gateway_client.resize_ipv6_gateway(gateway_id, bandwidthInMbps)
        return res
    except exception.BceHttpClientError as e:
        # 异常处理
        print(e.last_error)
        print(e.request_id)
        print(e.code)
        return None


if __name__ == "__main__":
    # create a ipv6 gateway client
    HOST = b''
    AK = b''
    SK = b''
    config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

    ipv6gateway_client = IPv6GatewayClient(config)
    gateway_id = b'ipv6-xx'

    res = test_resize_ipv6_gateway(ipv6gateway_client, gateway_id, bandwidthInMbps=10)
