# Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
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
Samples for bcm client.
"""

# !/usr/bin/env python
# coding=utf-8
from baidubce.exception import BceHttpClientError, BceServerError
from baidubce.services.bcm.bcm_client import BcmClient, bcm_model
import bcm_sample_conf

if __name__ == '__main__':

    import logging

    logging.basicConfig(level=logging.DEBUG)
    __logger = logging.getLogger(__name__)

    user_id = "fakeuser1ba678asdf8as7df6a5sdf67"
    scope = "BCE_BCC"
    metric_name = "vCPUUsagePercent"
    metric_name_batch = "CPUUsagePercent,MemUsagePercent"
    dimensions = "InstanceId:i-xxx"
    dimensions_batch = "InstanceId:i-1xx,InstanceId:i-2xx"
    statistics = "average,maximum,minimum"
    start_time = "2020-01-20T00:00:01Z"
    end_time = "2020-01-20T00:10:01Z"
    period_in_second = 60

    # create a bcm client
    bcm_client = BcmClient(bcm_sample_conf.config)

    # query metric data from bcm interface
    try:
        response = bcm_client.get_metric_data(user_id=user_id,
                                              scope=scope,
                                              metric_name=metric_name,
                                              dimensions=dimensions,
                                              statistics=statistics,
                                              start_time=start_time,
                                              end_time=end_time,
                                              period_in_second=period_in_second)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # query batch metric data from bcm interface
    try:
        response = bcm_client.get_batch_metric_data(user_id=user_id,
                                                    scope=scope,
                                                    metric_name=metric_name_batch,
                                                    dimensions=dimensions_batch,
                                                    statistics=statistics,
                                                    start_time=start_time,
                                                    end_time=end_time,
                                                    period_in_second=period_in_second)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # delete a custom namespace from bcm interface
    try:
        names = ["Test01"]
        response = bcm_client.batch_delete_namespaces(user_id=user_id, names=names)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # create a custom namespace for custom monitor from bcm interface
    try:
        name = "Test01"
        namespace_alias = "test"
        comment = "test"
        response = bcm_client.create_namespace(user_id=user_id, name=name,
                                               namespace_alias=namespace_alias, comment=comment)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # update a custom namespace from bcm interface
    try:
        name = "Test01"
        namespace_alias = "test01"
        comment = "test01"
        response = bcm_client.update_namespace(user_id=user_id, name=name,
                                               namespace_alias=namespace_alias, comment=comment)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list custom namespaces from bcm interface
    try:
        response = bcm_client.list_namespaces(user_id=user_id)
        print(response)

        name = "test"
        page_no = 1
        page_size = 10
        response = bcm_client.list_namespaces(user_id=user_id, name=name, page_no=page_no, page_size=page_size)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # create custom metric from bcm interface
    try:
        namespace = "Test01"
        metric_name_without_dimension = "TestMetric01"
        metric_alias = "test"
        unit = "sec"
        cycle = 60
        response = bcm_client.create_namespace_metric(user_id=user_id, namespace=namespace,
                                                      metric_name=metric_name_without_dimension,
                                                      metric_alias=metric_alias, unit=unit, cycle=cycle)
        print(response)

        metric_name_dimension = "TestMetric02"
        metric_dimensions = [bcm_model.CustomDimensionModel("test", 1, alias="test")]
        response = bcm_client.create_namespace_metric(user_id=user_id, namespace=namespace,
                                                      metric_name=metric_name_dimension, metric_alias=metric_alias,
                                                      unit=unit, cycle=cycle, dimensions=metric_dimensions)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # update custom metric from bcm interface
    try:
        namespace = "Test01"
        metric_name_without_dimension = "TestMetric01"
        metric_alias = "test01"
        unit = "sec"
        cycle = 60
        response = bcm_client.update_namespace_metric(user_id=user_id, namespace=namespace,
                                                      metric_name=metric_name_without_dimension,
                                                      metric_alias=metric_alias, unit=unit, cycle=cycle)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list custom metrics from bcm interface
    try:
        namespace = "Test01"
        response = bcm_client.list_namespace_metrics(user_id=user_id, namespace=namespace)
        print(response)

        namespace = "Test01"
        metric_name = "test"
        metric_alias = "test"
        page_no = 1
        page_size = 10
        response = bcm_client.list_namespace_metrics(user_id=user_id, namespace=namespace, metric_name=metric_name,
                                                     metric_alias=metric_alias, page_no=page_no, page_size=page_size)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # get custom metric from bcm interface
    custom_metric_ids = []
    try:
        namespace = "Test01"
        metric_name = "TestMetric01"
        response = bcm_client.get_custom_metric(user_id=user_id, namespace=namespace, metric_name=metric_name)
        print(response)
        if response.id is not None:
            custom_metric_ids.append(response.id)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # batch delete custom metrics from bcm interface
    try:
        namespace = "Test01"
        ids = custom_metric_ids
        response = bcm_client.batch_delete_namespace_metrics(user_id=user_id, namespace=namespace, ids=ids)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # create custom event from bcm interface
    try:
        namespace = "Test01"
        event_name = "TestEvent01"
        event_name_alias = "test"
        event_level = bcm_model.EventLevel.NOTICE
        comment = "test"
        response = bcm_client.create_namespace_event(user_id=user_id, namespace=namespace, event_name=event_name,
                                                     event_name_alias=event_name_alias, event_level=event_level,
                                                     comment=comment)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # update custom event from bcm interface
    try:
        namespace = "Test01"
        event_name = "TestEvent01"
        event_name_alias = "test01"
        event_level = bcm_model.EventLevel.NOTICE
        comment = "test01"
        response = bcm_client.update_namespace_event(user_id=user_id, namespace=namespace, event_name=event_name,
                                                     event_name_alias=event_name_alias, event_level=event_level,
                                                     comment=comment)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list custom events from bcm interface
    try:
        namespace = "Test01"
        response = bcm_client.list_namespace_events(user_id=user_id, namespace=namespace)
        print(response)

        namespace = "Test01"
        event_name = "test"
        event_level = bcm_model.EventLevel.NOTICE
        page_no = 1
        page_size = 10
        response = bcm_client.list_namespace_events(user_id=user_id, namespace=namespace, name=event_name,
                                                    event_level=event_level, page_no=page_no, page_size=page_size)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # get custom event from bcm interface
    try:
        namespace = "Test01"
        event_name = "TestEvent01"
        response = bcm_client.get_custom_event(user_id=user_id, namespace=namespace, event_name=event_name)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # batch delete custom events from bcm interface
    try:
        namespace = "Test01"
        names = ["TestEvent01"]
        response = bcm_client.batch_delete_namespace_events(user_id=user_id, namespace=namespace, names=names)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list notify group
    try:
        response = bcm_client.list_notify_group(page_no=1, page_size=10)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list notify party
    try:
        response = bcm_client.list_notify_party(name="test", page_no=1, page_size=5)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # create action
    try:
        notification = bcm_model.Notification("EMAIL")
        member = bcm_model.Member("notifyParty", "56c9e0e2138c4f", "lzs")
        response = bcm_client.create_action(user_id, [notification], [member], "test_wjr_py")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # delete action
    try:
        response = bcm_client.delete_action(user_id=user_id, name="bb832cf9-ce5e-4c59-85a0-4ddf30******")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list action
    try:
        response = bcm_client.list_action(user_id=user_id, page_no=1, page_size=5, name="test")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # update action
    try:
        notification = bcm_model.Notification("EMAIL")
        member = bcm_model.Member("notifyParty", "56c9e0e2138c4f", "lzs")
        response = bcm_client.update_action(user_id=user_id, notifications=[notification], members=[member],
                                            alias="test_wjr_py", disable_times=[], action_callbacks=[],
                                            name="2185c71a-9132-4b4e-92d2-35eebd******")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # log extract
    try:
        extract_rule = ("800] \"(?<method>(GET|POST|PUT|DELETE)) .*/v1/dashboard/metric/(?<widget>(cycle|trend|report|"
                        "billboard|gaugechart)) HTTP/1.1\".* (?<resTime>[0-9]+)ms")
        log_example = (
            "10.157.16.207 - - [09/Apr/2020:20:45:33 +0800] \"POST /v1/dashboard/metric/gaugechart HTTP/1.1\""
            " 200 117 109ms")
        response = bcm_client.log_extract(user_id=user_id, extract_rule=extract_rule, log_example=log_example)
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # query metric meta for_application
    try:
        response = bcm_client.query_metric_meta_for_application(user_id=user_id, app_name="test14",
                                                                task_name="79c35af26c4346ab844bcbcdde******",
                                                                metric_name="log.responseTime",
                                                                dimension_keys=["method"])
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # query metric data for_application
    try:
        response = bcm_client.query_metric_data_for_application(user_id=user_id, app_name="zmq-log-1115",
                                                                task_name="6d3f07e6684d47b69ca9600f7f******",
                                                                metric_name="exec.6d3f07e6684d47b69ca9600f******"
                                                                            ".metric1",
                                                                start_time="2023-12-05T09:54:15Z",
                                                                end_time="2023-12-05T10:04:15Z",
                                                                instances=["0.zmq-log-1115"],
                                                                statistics=["average", "maximum"])
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list alarm metrics for application
    try:
        response = bcm_client.list_alarm_metrics_for_application(user_id=user_id, app_name="test_ymd_app_0918",
                                                                  task_name="46e78b2831394f738429f8826******",
                                                                  search_name="test_name")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # test get alarm policy for application
    try:
        response = bcm_client.get_alarm_policy_for_application(user_id=user_id, app_name="test_ymd_app_0918",
                                                                alarm_name="inst-test")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # delete alarm policy for application
    try:
        response = bcm_client.delete_alarm_policy_for_application(user_id=user_id, app_name="uuu", alarm_name="dasd")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # list alarm policy for application
    try:
        response = bcm_client.list_alarm_policy_for_application(user_id=user_id, page_no=1, src_type="PORT")
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # create alarm policy for application
    try:
        monito_object_view = bcm_model.ApplicationObjectView("zmq-log-1115.453bf9588c9e488f9ba2c98412******")
        monitor_object = bcm_model.ApplicationMonitorObject("APP", [monito_object_view])
        rule = bcm_model.ApplicationAlarmRule("log.ab3b543f41974e26ab984d94fc******.log_metric2", "log_metric2",
                                              60, "average", 10, ">", 1,
                                              0, [])
        response = bcm_client.create_alarm_policy_for_application(user_id, "", "test_wjr_py",
                                                                   "zmq-log-1115", "APP",
                                                                   monitor_object, "ab3b543f41974e26ab984d94fc******",
                                                                   "LOG", "INSTANCE", "MAJOR",
                                                                   [[rule]], incident_actions=[
                                                                            "624c99b5-5436-478c-8326-0efc81******"])
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

    # update alarm policy for application
    try:
        monito_object_view = bcm_model.ApplicationObjectView("zmq-log-1115.453bf9588c9e488f9ba2c98412******")
        monitor_object = bcm_model.ApplicationMonitorObject("APP", [monito_object_view])
        rule = bcm_model.ApplicationAlarmRule("log.ab3b543f41974e26ab984d94fc******.log_metric2", "log_metric2",
                                              60, "average", 10, ">", 1,
                                              0, [])
        response = bcm_client.update_alarm_policy_for_application(user_id, "", "test_wjr_py",
                                                                   "zmq-log-1115", "APP",
                                                                   monitor_object, "ab3b543f41974e26ab984d94fc******",
                                                                   "LOG", "INSTANCE", "MAJOR",
                                                                   [[rule]], incident_actions=[
                "624c99b5-5436-478c-8326-0efc8******"])
        print(response)
    except BceHttpClientError as e:
        if isinstance(e.last_error, BceServerError):
            __logger.error('send request failed. Response %s, code: %s, msg: %s'
                           % (e.last_error.status_code, e.last_error.code, e.last_error.message))
        else:
            __logger.error('send request failed. Unknown exception: %s' % e)

