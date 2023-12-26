# -*- coding: utf-8 -*-

"""
This module for test et channel route rule.
"""
import sys
import uuid
import unittest

from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.et import et_channel_route_rule_client

et_id = ''
et_channel_id = ''

if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf-8')

def generate_client_token_by_uuid():
    """
    The default method to generate the random string for client_token
    if the optional parameter client_token is not specified by the user.
    :return:
    :rtype string
    """
    return str(uuid.uuid4())

generate_client_token = generate_client_token_by_uuid

class TestEtClient(unittest.TestCase):
    """
    unit test
    """

    def setUp(self):
        """
        set up
        """
        HOST = b'host'
        AK = b'ak'
        SK = b'sk'
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
        self.client = et_channel_route_rule_client.EtChannelRouteRuleClient(config)

    def test_create_et_channel_route_rule(self):
        """
        test create et channel route rule
        """
        client_token = generate_client_token()
        dest_address = "192.168.0.7/32" 
        nexthop_type = "etChannel"
        nexthop_id = ""
        resp = self.client.create_et_channel_route_rule(et_id, et_channel_id, dest_address,
            nexthop_type, nexthop_id, client_token=client_token)
        print(resp)

    def test_list_et_channel_route_rule(self):
        """
        test list et channel route rule
        """
        client_token = generate_client_token()
        resp = self.client.list_et_channel_route_rules(et_id, et_channel_id, client_token=client_token)
        print(resp)

    def test_update_et_channel_route_rule(self):
        """
        test update et channel route rule
        """
        client_token = generate_client_token()
        route_rule_id = ""
        description = "test_update"
        resp = self.client.update_et_channel_route_rule(et_id, et_channel_id, route_rule_id,
            description, client_token=client_token)
        print(resp)

    def test_delete_et_channel_route_rule(self):
        """
        test delete et channel route rule
        """
        client_token = generate_client_token()
        route_rule_id = ""
        resp = self.client.delete_et_channel_route_rule(et_id, et_channel_id, route_rule_id,
            client_token=client_token)
        print(resp)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(TestEtClient("test_create_et_channel_route_rule"))
    #suite.addTest(TestEtClient("test_update_et_channel_route_rule"))
    #suite.addTest(TestEtClient("test_list_et_channel_route_rule"))
    #suite.addTest(TestEtClient("test_delete_et_channel_route_rule"))
    runner = unittest.TextTestRunner()
    runner.run(suite)