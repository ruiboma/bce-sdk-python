# !/usr/bin/env python
# coding=utf-8
"""
Samples for ipv6gateway client.
"""
import uuid

from baidubce import exception
from baidubce.services.ipv6gateway import ipv6gateway_model
from baidubce.services.ipv6gateway.ipv6gateway_client import IPv6GatewayClient
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials


def generate_client_token_by_uuid():
    """
    The default method to generate the random string for client_token
    if the optional parameter client_token is not specified by the user.

    :return:
    :rtype string
    """
    return str(uuid.uuid4())


def test_create_ipv6_gateway(ipv6gateway_client, client_token, name, VPC_ID, bandwidthInMbps, billing):
    """
    create ipv6 gateway.

    :param client_token:
        An ASCII string whose length is less than 64.
        The request will be idempotent if clientToken is provided.
        If the clientToken is not specified by user,
        a random String generated by default algorithm will be used.
    :type client_token: string

    :param name:
        ipv6 gateway's name
    :type name: string

    :param VPC_ID:
        the VPC ID of the nat.
    :type VPC_ID: string

    :param bandwidthInMbps:
        bandwidth of the ipv6 gateway.
    :type bandwidthInMbps: int

    :param billing:
        billing info
    :type billing: nat_model.Billing

    :return:
    :rtype baidubce.bce_response.BceResponse

    Raise:
        BceHttpClientError: http request error
    """
    try:
        res = ipv6gateway_client.create_ipv6_gateway(client_token=client_token, name=name,
                                                     vpc_id=VPC_ID, bandwidthInMbps=bandwidthInMbps,
                                                     billing=billing)
        return res
    except exception.BceHttpClientError as e:
        # 异常处理
        print(e.last_error)
        print(e.request_id)
        print(e.code)
        return None


if __name__ == "__main__":
    post_paid_billing = ipv6gateway_model.Billing('Postpaid')
    VPC_ID = b'vpc-xx'

    # create a ipv6 gateway client
    HOST = b''
    AK = b''
    SK = b''
    config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)

    ipv6gateway_client = IPv6GatewayClient(config)
    client_token = generate_client_token_by_uuid()
    name = 'ipv6_gateway_' + client_token
    res = test_create_ipv6_gateway(ipv6gateway_client, client_token, name, VPC_ID, bandwidthInMbps=10,
                                   billing=post_paid_billing)

    print(res)
    print(res.ipv6_gateway_id)
