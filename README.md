# Prometheus Status

## About

This project solves a problem when we use prometheus in statefulset mode with replicas and high availability.
when the pod fails and prometheus can't recover, this application monitors the status of the pods, one of the failing pods sends an alert to the alertmanager webhook notifying the defined alert channels.

## Pre-reqs

- k8s
- helm v2
- Python 3

## Build

### Build Docker image

```sh
$ docker  build -t wellbastos/prometheus-status:latest .
``` 
### Pushing docker image to registry:

```sh
docker push wellbastos/prometheus-status:latest 
```

## Deploy

### Install

```sh
$ helm install -n prometheus-status --namespace monitoring -f prometheus-status/values.yaml prometheus-status/
```

### Upgrade

```sh
$ helm upgrade prometheus-status -f prometheus-status/values.yaml prometheus-status/
```

### Unistall

```sh
$ helm del --purge prometheus-status
```

## created by:

 Wellington Bastos
 email: wellingtonbastos@hotmail.com
 Linkedin: https://www.linkedin.com/in/wellingtonbastos/