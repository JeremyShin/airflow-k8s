# kind, helm 설치

```shell
# kind 설치
brew install kind

# kubectl 설치 확인
kubectl version

# helm 설치
brew install helm
```

# colima 설정
```
colima start --cpu 6 --memory 12
```

# kube-ps1 설정
* oh-my-zsh에서 plugins에 kube-ps1 추가
plugins=(
git
...
kube-ps1
)

source $ZSH/oh-my-zsh.sh
PROMPT= '$(kube_ps1)' $PROMPT


# kind 클러스터 생성

# kind-config.yaml 파일 생성
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4

# 단일 노드 사용
nodes:
    - role: control-plane

```

# kind 클러스터 생성

```shell
kind create cluster --name airflow-cluster --config kind-config.yaml
```
# kind 클러스터 생성 확인
```shell
kind get clusters
# airflow-cluster
```

* 컨텍스트 확인
```shell
k config get-contexts
```


# Helm repo 등록 & 업데이트
```shell
helm repo add airflow-stable https://airflow-helm.github.io/charts
helm repo update
```

# airflow 설치
```shell
helm install airflow airflow-stable/airflow --namespace airflow --create-namespace -f values.yaml
```

# 설치 확인 & 접속
```shell
# pod 상태 확인
kubectl get pods -n airflow
```

```
# 웹 UI 포트포워딩
kubectl port-forward svc/airflow-web 8080:8080 -n airflow
```

### helm 차트 업데이트 반영
```shell
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f values.yaml --debug
```

### pod 접속
```shell
k exec -it airflow-scheduler-699495d87-dtx94 --namespace airflow -- /bin/bash
```
