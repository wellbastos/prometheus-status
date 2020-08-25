#!/usr/bin/env python3
from kubernetes import client, config
from alertmanager import AlertManager, Alert
from logging2 import Logger
import requests
import json

# run local before test
# config.load_kube_config()
# run at cluster auth by role 
config.load_incluster_config()
# Compatibilities at api 1.16
v1 = client.AppsV1Api()

logger  = Logger("Prometheus-Status")

try:
    pod_list = v1.list_namespaced_stateful_set("monitoring")
    for pod in pod_list.items:
        pod.metadata.name, pod.status.ready_replicas

    prom = pod.status.ready_replicas

    host = "http://prometheus-alertmanager.monitoring.svc.cluster.local"
    port  = 80
    
    r = requests.get( host )

    if r.status_code != 200:
        logger.error("Prometheus-Status: Not connected to Alertmanager!")
        exit(1)

    if prom != 2:
        data = {
                    "labels": {
                        "alertname": "Prometheus Down",
                        "severity": "critical"
                    },
                    "annotations": {
                        "description": "One of Prometheus pod has problem!",
                        "summary": "PROMETHEUS - Prometheus Down"
                    }
                }

        a_manager = AlertManager(host=host,port=port)
        a_manager.post_alerts(Alert.from_dict(data))      
        
        # print message local test
        # print(Alert.from_dict(data))
        logger.error("Prometheus instance is down!")
        
    else:
        logger.info("Prometheus is running!")

except Exception as e:
    logger.exception("%s"%(e))
    
exit(0)