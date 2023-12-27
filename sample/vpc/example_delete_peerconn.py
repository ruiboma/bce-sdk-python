# -*- coding: utf-8 -*-
"""
example for delete peerconn.
"""

import uuid

from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.exception import BceHttpClientError
from baidubce.services.vpc import peerconn_client

if __name__ == "__main__":
    ak = "Your AK"
    sk = "Your SK"
    endpoint = "bcc.bj.baidubce.com"
    config = BceClientConfiguration(credentials=BceCredentials(access_key_id=ak, secret_access_key=sk),
                                    endpoint=endpoint)
    peerconn_client = peerconn_client.PeerConnClient(config)
    try:
        resp = peerconn_client.delete_peerconn(peer_conn_id="peerconn-9td54fmx143e",
                                               client_token=str(uuid.uuid4()))
        print("Delete peerconn response: %s", resp)
    except BceHttpClientError as e:
        print("Exception when calling api: %s" % e)