# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.

"""
Unit tests for bcc client.
"""
import json
import os
import random
import string
import sys
import unittest
import uuid

import baidubce
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.bcc import bcc_client
from baidubce.services.bcc import bcc_model
from baidubce.services.bcc.bcc_model import EphemeralDisk

file_path = os.path.normpath(os.path.dirname(__file__))
sys.path.append(file_path + '/../../')
reload(sys)
sys.setdefaultencoding('utf-8')


HOST = 'http://bcc.bce-api.baidu.com'
AK = '4f4b13eda66e42e29225bb02d9193a48'
SK = '507b4a729f6a44feab398a6a5984304d'

instance_id = 'i-gJVyzFlv'
volume_id = 'v-QtHXNLWa'
image_id = 'm-32s5YYqD'
snapshot_id = 's-Ro9vAnQE'
system_snapshot_id = 's-hnsVUGIw'
security_group_id = 'g-hweloYd8'

post_paid_billing = bcc_model.Billing('Postpaid', 1)
pre_paid_billing = bcc_model.Billing('Prepaid', 1)

force_stop = False
admin_pass = 'test@baidu'


def generate_client_token_by_random():
    """
    The alternative method to generate the random string for client_token 
    if the optional parameter client_token is not specified by the user.
    :return:
    :rtype string    
    """
    client_token = ''.join(random.sample(string.ascii_letters + string.digits, 36))
    return client_token


def generate_client_token_by_uuid():
    """
    The default method to generate the random string for client_token 
    if the optional parameter client_token is not specified by the user.
    :return:
    :rtype string    
    """
    return str(uuid.uuid4())


generate_client_token = generate_client_token_by_uuid


class TestBccClient(unittest.TestCase):
    """
    Test class for bcc sdk client
    """
    def setUp(self):        
        config = BceClientConfiguration(credentials=BceCredentials(AK, SK), 
                        endpoint=HOST)
        self.client = bcc_client.BccClient(config)

    def test_create_instance(self):
        """
        test case for create_instance
        """ 
        instance_type = 'bcc.t1.tiny'
        client_token = generate_client_token()
        instance_name = 'test_instance_' + client_token
        self.assertEqual(
            type(self.client.create_instance(instance_type,
                                             image_id,
                                             name=instance_name,
                                             client_token=client_token)),
            baidubce.bce_response.BceResponse)

    def test_create_instance_by_cpu_memory(self):
        """
        test case for create_instance_by_cpu_memory
        :return:
        """
        client_token = generate_client_token()
        instance_name = 'test_instance_' + client_token
        self.assertEqual(
            type(self.client.create_instance(1, 1,
                                             image_id,
                                             name=instance_name,
                                             billing=post_paid_billing,
                                             client_token=client_token)),
            baidubce.bce_response.BceResponse)

    def test_create_instance_from_dedicated_host(self):
        """
        test case for create instance from dedicated host
        """
        ephemeral_disk = EphemeralDisk(6144)
        ephemeral_disks = [ephemeral_disk.__dict__, ephemeral_disk.__dict__]
        self.client.create_instance_from_dedicated_host(1, 2, 'm-32s5YYqD', 'd-MPgs6jPr',
                                                        ephemeral_disks)

    def test_list_instances(self):
        """
        test case for list_instances
        """       
        self.assertEqual(
            type(self.client.list_instances()),
            baidubce.bce_response.BceResponse)

    def test_get_instance(self):
        """
        test case for get_instance
        """      
        self.assertEqual(
            type(self.client.get_instance(instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_start_instance(self):
        """
        test case for start_instance
        """   
        self.assertEqual(
            type(self.client.start_instance(instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_stop_instance(self):
        """
        test case for stop_instance
        """   
        self.assertEqual(
            type(self.client.stop_instance(instance_id,
                                           force_stop)), 
            baidubce.bce_response.BceResponse)

    def test_reboot_instance(self):
        """
        test case for reboot_instance
        """ 
        self.assertEqual(
            type(self.client.reboot_instance(instance_id,
                                             force_stop)), 
            baidubce.bce_response.BceResponse)

    def test_modify_instance_password(self):
        """
        test case for modify_instance_password
        """     
        self.assertEqual(
            type(self.client.modify_instance_password(instance_id,
                                                      admin_pass)), 
            baidubce.bce_response.BceResponse)

    def test_modify_instance_attributes(self):
        """
        test case for modify_instance_attributes
        """ 
        name = 'name_modify'    
        self.assertEqual(
            type(self.client.modify_instance_attributes(instance_id,
                                                        name)), 
            baidubce.bce_response.BceResponse)

    def test_rebuild_instance(self):
        """
        test case for rebuild_instance
        """     
        self.assertEqual(
            type(self.client.rebuild_instance(instance_id,
                                              image_id,
                                              admin_pass)), 
            baidubce.bce_response.BceResponse)

    def test_release_instance(self):
        """
        test case for release_instance
        """ 
        self.assertEqual(
            type(self.client.release_instance(instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_resize_instance(self):
        """
        test case for resize_instance
        """ 
        client_token = generate_client_token()
        self.assertEqual(
            type(self.client.resize_instance(instance_id,
                                             1, 2,
                                             client_token)), 
            baidubce.bce_response.BceResponse)

    def test_bind_instance_to_security_group(self):
        """
        test case for bind_instance_to_security_group
        """     
        self.assertEqual(
            type(self.client.bind_instance_to_security_group(instance_id,
                                                             security_group_id)), 
            baidubce.bce_response.BceResponse)

    def test_unbind_instance_from_security_group(self):
        """
        test case for unbind_instance_from_security_group
        """     
        self.assertEqual(
            type(self.client.unbind_instance_from_security_group(instance_id,
                                                                 security_group_id)), 
            baidubce.bce_response.BceResponse)

    def test_get_instance_vnc(self):
        """
        test case for get_instance_vnc
        """ 
        self.assertEqual(
            type(self.client.get_instance_vnc(instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_purchase_reserved_instance(self):
        """
        test case for purchase_reserved_instance
        """ 
        billing = pre_paid_billing
        client_token = generate_client_token()
        self.assertEqual(
            type(self.client.purchase_reserved_instance(instance_id,
                                                        billing,
                                                        client_token)), 
            baidubce.bce_response.BceResponse)

    def test_list_instance_specs(self):
        """
        test case for list_instance_specs
        """ 
        self.assertEqual(
            type(self.client.list_instance_specs()), 
            baidubce.bce_response.BceResponse)

    def test_create_volume_with_cds_size(self):
        """
        test case for create_volume_with_cds_size
        """ 
        client_token = generate_client_token()
        billing = pre_paid_billing
        cds_size_in_gb = 5
        create_response = self.client.create_volume_with_cds_size(cds_size_in_gb,
                                                                  zone_name='cn-bj-a',
                                                                  client_token=client_token)
        print create_response
        self.assertEqual(
            type(create_response),
            baidubce.bce_response.BceResponse)

    def test_create_volume_with_snapshot_id(self):
        """
        test case for create_volume_with_snapshot_id
        """ 
        client_token = generate_client_token()
        self.assertEqual(
            type(self.client.create_volume_with_snapshot_id(snapshot_id,
                                                            client_token=client_token)), 
            baidubce.bce_response.BceResponse)

    def test_list_volumes(self):
        """
        test case for list_volumes
        """
        volume_list = self.client.list_volumes(zone_name='cn-bj-b')
        print volume_list
        self.assertEqual(
            type(volume_list),
            baidubce.bce_response.BceResponse)

    def test_get_volume(self):
        """
        test case for get_volume
        """      
        self.assertEqual(
            type(self.client.get_volume(volume_id)), 
            baidubce.bce_response.BceResponse)

    def test_attach_volume(self):
        """
        test case for attach_volume
        """      
        self.assertEqual(
            type(self.client.attach_volume(volume_id, 
                                        instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_detach_volume(self):
        """
        test case for detach_volume
        """      
        self.assertEqual(
            type(self.client.detach_volume(volume_id, 
                                           instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_release_volume(self):
        """
        test case for release_volume
        """      
        self.assertEqual(
            type(self.client.release_volume(volume_id)), 
            baidubce.bce_response.BceResponse)

    def test_resize_volume(self):
        """
        test case for resize_volume
        """  
        resize_cds_size_in_gb = 10
        client_token = generate_client_token()    
        self.assertEqual(
            type(self.client.resize_volume(volume_id,
                                           resize_cds_size_in_gb,
                                           client_token)), 
            baidubce.bce_response.BceResponse)

    def test_rollback_volume(self):
        """
        test case for rollback_volume
        """      
        self.assertEqual(
            type(self.client.rollback_volume(volume_id,
                                            snapshot_id)), 
            baidubce.bce_response.BceResponse)

    def test_purchase_reserved_volume(self):
        """
        test case for purchase_reserved_volume
        """  
        billing = pre_paid_billing
        client_token = generate_client_token()    
        self.assertEqual(
            type(self.client.purchase_reserved_volume(volume_id,
                                                      billing,
                                                      client_token)), 
            baidubce.bce_response.BceResponse)

    def test_create_image_from_instance_id(self):
        """
        test case for create_image_from_instance_id
        """ 
        client_token = generate_client_token()
        image_name = 'test_image_from_instance_' + client_token
        self.assertEqual(
            type(self.client.create_image_from_instance_id(image_name,
                                                           instance_id=instance_id,
                                                           client_token=client_token)), 
            baidubce.bce_response.BceResponse)

    def test_create_image_from_snapshot_id(self):
        """
        test case for create_image_from_snapshot_id
        """ 
        client_token = generate_client_token()
        image_name = 'test_image_from_snapshot_' + client_token
        self.assertEqual(
            type(self.client.create_image_from_snapshot_id(image_name,
                                                           snapshot_id=system_snapshot_id,
                                                           client_token=client_token)), 
            baidubce.bce_response.BceResponse)

    def test_list_images(self):
        """
        test case for list_images
        """       
        self.assertEqual(
            type(self.client.list_images()), 
            baidubce.bce_response.BceResponse)

    def test_get_image(self):
        """
        test case for get_image
        """      
        self.assertEqual(
            type(self.client.get_image(image_id)), 
            baidubce.bce_response.BceResponse)

    def test_delete_image(self):
        """
        test case for delete_image
        """      
        self.assertEqual(
            type(self.client.delete_image(image_id)), 
            baidubce.bce_response.BceResponse)

    def test_create_snapshot(self):
        """
        test case for create_snapshot
        """ 
        client_token = generate_client_token()
        snapshot_name = 'test_snapshot_' + client_token
        self.assertEqual(
            type(self.client.create_snapshot(volume_id,
                                             snapshot_name,
                                             client_token=client_token)), 
            baidubce.bce_response.BceResponse)

    def test_list_snapshots(self):
        """
        test case for list_snapshots
        """       
        self.assertEqual(
            type(self.client.list_snapshots()), 
            baidubce.bce_response.BceResponse)

    def test_get_snapshot(self):
        """
        test case for get_snapshot
        """      
        self.assertEqual(
            type(self.client.get_snapshot(snapshot_id)), 
            baidubce.bce_response.BceResponse)

    def test_delete_snapshot(self):
        """
        test case for delete_snapshot
        """      
        self.assertEqual(
            type(self.client.delete_snapshot(snapshot_id)), 
            baidubce.bce_response.BceResponse)

    def test_create_security_group(self):
        """
        test case for create_security_group
        """ 
        client_token = generate_client_token()
        security_group_name = 'test_security_group_' + client_token
        security_group_rule = bcc_model.SecurityGroupRuleModel('test_rule_' + client_token,
                                                               'ingress',
                                                               portRange='1-65535',
                                                               protocol='tcp',
                                                               sourceGroupId='',
                                                               sourceIp='')
        security_group_rule_list = []
        security_group_rule_list.append(security_group_rule)
        self.assertEqual(
            type(self.client.create_security_group(name=security_group_name,
                                                   rules=security_group_rule_list,
                                                   client_token=client_token)), 
            baidubce.bce_response.BceResponse)

    def test_list_security_groups(self):
        """
        test case for list_security_groups
        """       
        self.assertEqual(
            type(self.client.list_security_groups(instance_id=instance_id)), 
            baidubce.bce_response.BceResponse)

    def test_delete_security_group(self):
        """
        test case for delete_security_group
        """      
        self.assertEqual(
            type(self.client.delete_security_group(security_group_id)), 
            baidubce.bce_response.BceResponse)

    def test_authorize_security_group_rule(self):
        """
        test case for authorize_security_group_rule
        """
        security_group_rule = bcc_model.SecurityGroupRuleModel(direction='ingress',
                                                               portRange='80-90',
                                                               protocol='tcp')
        print self.client.authorize_security_group_rule("g-RrAecfjQ", security_group_rule)

    def test_revoke_security_group_rule(self):
        """
        test case for revoke_security_group_rule
        """
        security_group_rule = bcc_model.SecurityGroupRuleModel(direction='ingress',
                                                               portRange='80-90',
                                                               protocol='tcp')
        print self.client.revoke_security_group_rule("g-RrAecfjQ", security_group_rule)

    def test_list_zones(self):
        """
        test case for list_zones
        """
        print self.client.list_zones()

    def test_get_private_ip_list(self):
        """
        test case for get_private_ip
        """
        print self.client.get_private_ip_list('i-gDwqItW2')

    def test_assign_private_ip_to_instance(self):
        """
        test for assign_private_ip_to_instance
        """
        print self.client.assign_private_ip_to_instance('i-gDwqItW2', '192.168.0.12')

    def test_unassign_private_ip_from_instance(self):
        """
        test case for unassign_priv
        :return:
        """
        print self.client.unassign_private_ip_from_instance('i-gDwqItW2', '192.168.0.12')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    # suite.addTest(TestBccClient("test_create_instance"))
    # suite.addTest(TestBccClient("test_create_instance_by_cpu_memory"))
    # suite.addTest(TestBccClient("test_create_instance_from_dedicated_host"))
    # suite.addTest(TestBccClient("test_create_volume_with_cds_size"))
    # suite.addTest(TestBccClient("test_create_volume_with_snapshot_id"))
    # suite.addTest(TestBccClient("test_create_image_from_instance_id"))
    # suite.addTest(TestBccClient("test_create_image_from_snapshot_id"))
    # suite.addTest(TestBccClient("test_create_snapshot"))
    # suite.addTest(TestBccClient("test_create_security_group"))

    # suite.addTest(TestBccClient("test_get_private_ip_list"))
    # suite.addTest(TestBccClient("test_assign_private_ip_to_instance"))
    # suite.addTest(TestBccClient("test_unassign_private_ip_from_instance"))

    suite.addTest(TestBccClient("test_list_instances"))
    # suite.addTest(TestBccClient("test_list_volumes"))
    # suite.addTest(TestBccClient("test_list_images"))
    # suite.addTest(TestBccClient("test_list_snapshots"))
    # suite.addTest(TestBccClient("test_list_security_groups"))
    # suite.addTest(TestBccClient("test_get_instance"))
    # suite.addTest(TestBccClient("test_get_instance_vnc"))
    # suite.addTest(TestBccClient("test_list_instance_specs"))
    # suite.addTest(TestBccClient("test_get_volume"))
    # suite.addTest(TestBccClient("test_get_image"))
    # suite.addTest(TestBccClient("test_get_snapshot"))

    # suite.addTest(TestBccClient("test_modify_instance_password"))
    # suite.addTest(TestBccClient("test_resize_instance"))
    # suite.addTest(TestBccClient("test_release_instance"))
    # suite.addTest(TestBccClient("test_delete_snapshot"))
    # suite.addTest(TestBccClient("test_delete_security_group"))

    # suite.addTest(TestBccClient("test_authorize_security_group_rule"))
    # suite.addTest(TestBccClient("test_revoke_security_group_rule"))

    # suite.addTest(TestBccClient("test_list_zones"))

    runner = unittest.TextTestRunner()
    runner.run(suite)

