
# AIRFLOW HELM 검색 후 다운
```shell
helm repo list
helm search repo airflow
helm search repo apache-airflow/airflow --versions
helm pull apache-airflow/airflow --version 1.16.0
tar -xvf airflow-1.16.0.tgz
```

# Prometheus Helm 다운
```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
# kube-prometheus-stack 설치 (Prometheus, Alertmanager, Operator, Grafana 포함)
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

# Prometheus 웹서버
```shell
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n monitoring
# localhost:9090
```
