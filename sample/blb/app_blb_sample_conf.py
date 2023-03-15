# !/usr/bin/env python
# coding=utf-8
"""
Configuration for app blb samples.
"""
import logging
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

HOST = b'host'
AK = b'ak'
SK = b'sk'
blbId = b''
appServerGroupId = ''
portId = ''
certIds = []

logger = logging.getLogger('baidubce.services.blb.app_blb_client')
fh = logging.FileHandler('sample.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

config = BceClientConfiguration(credentials=BceCredentials(AK, SK), endpoint=HOST)
