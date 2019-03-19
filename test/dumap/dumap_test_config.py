# -*- coding: UTF-8 -*-
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
Configurations for dumap client tests.
"""

import logging
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

HOST = b'lbs.baidubce.com'
# online AK SK
AK = b'b2171730f9fd4d8ea6b6e87902aa7016'
SK = b'1d868df398434647b5358e3b31d3927f'
# console app_id
APP_ID = b'4c34562f-2bf8-4bc1-85cf-6c7858d30c1b'

logger = logging.getLogger('baidubce.services.dumap.DumapClient')
fh = logging.FileHandler('test_dumap_client.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
config.retry_policy.max_error_retry = 0