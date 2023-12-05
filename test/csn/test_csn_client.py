# !/usr/bin/env python
# coding=UTF-8
#
# Copyright 2023 Baidu, Inc.
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
This module for test.
"""

import unittest

from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.csn import csn_client
from baidubce.services.csn import csn_model

csn_id = 'csn-xxxxxxxxxxxxxxxx'
csn_bp_id = 'csnBp-xxxxxxxxxxxx'
vpc_id = 'vpc-xxxxxxxxxxxx'

class TestCsnClient(unittest.TestCase):
    """
    unit test
    """

    def setUp(self):
        """
        set up
        """
        AK = b'ak'
        SK = b'sk'
        ENDPOINT = b'csn.baidubce.com'
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK),
                                        endpoint=ENDPOINT)
        self.the_client = csn_client.CsnClient(config)

    def tearDown(self):
        """
        tear down
        """
        self.the_client = None

    def test_create_csn(self):
        """
        test case for create_csn
        """
        print(self.the_client.create_csn('csn_unittest', 'csn_unittest desc'))

    def test_update_csn(self):
        """
        test case for update_csn
        """
        print(self.the_client.update_csn(csn_id, 'csn_unittest_update', 'csn_unittest_update desc'))

    def test_delete_csn(self):
        """
        test case for delete_csn
        """
        print(self.the_client.delete_csn(csn_id))

    def test_list_csn(self):
        """
        test case for list_csn
        """
        print(self.the_client.list_csn())

    def test_get_csn(self):
        """
        test case for get_csn
        """
        print(self.the_client.get_csn(csn_id))

    def test_attach_instance(self):
        """
        test case for attach_instance
        """
        print(self.the_client.attach_instance(csn_id, 'vpc', vpc_id, 'bj'))

    def test_list_instance(self):
        """
        test case for list_instance
        """
        print(self.the_client.list_instance(csn_id))

    def test_dettach_instance(self):
        """
        test case for dettach_instance
        """
        print(self.the_client.detach_instance(csn_id, 'vpc', vpc_id, 'bj'))

    def test_create_csn_bp(self):
        """
        test case for create_csn_bp
        """
        billing = csn_model.Billing('Prepaid', 1, 'month')
        print(self.the_client.create_csn_bp("csn_bp_unittest", 10, "China", "China", billing, "center"))

    def test_update_csn_bp(self):
        """
        test case for update_csn_bp
        """
        print(self.the_client.update_csn_bp(csn_bp_id, 'csn_bp_unittest_update'))

    def test_delete_csn_bp(self):
        """
        test case for delete_csn_bp
        """
        print(self.the_client.delete_csn_bp(csn_bp_id))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(TestCsnClient("test_create_csn"))
    # suite.addTest(TestCsnClient("test_update_csn"))
    # suite.addTest(TestCsnClient("test_delete_csn"))
    # suite.addTest(TestCsnClient("test_list_csn"))
    # suite.addTest(TestCsnClient("test_get_csn"))
    # suite.addTest(TestCsnClient("test_attach_instance"))
    # suite.addTest(TestCsnClient("test_list_instance"))
    # suite.addTest(TestCsnClient("test_dettach_instance"))
    # suite.addTest(TestCsnClient("test_create_csn_bp"))
    # suite.addTest(TestCsnClient("test_update_csn_bp"))
    # suite.addTest(TestCsnClient("test_delete_csn_bp"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
