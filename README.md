# TODO: k8spod, sparkk8s, emr on k8s operator 돌려보기
# iceberg, s3 table 테스트

# docker 설치
```shell
brew install docker

# m4 max
colima start --arch aarch64 --cpu 8 memory 32

# 상태 확인
docker version
```

# colima 설치
```shell
brew install colima

colima status
```

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
```shell
brew install kube-ps1

# ~/.zshrc
plugins=(
git
...
kube-ps1
)

source $ZSH/oh-my-zsh.sh
PROMPT= '$(kube_ps1)' $PROMPT
```

# kind 클러스터 생성

```shell
kind create cluster --name airflow-local --config app-chart/kind-config.yaml
```
# kind 클러스터 생성 확인
```shell
kind get clusters
# airflow-local
```

* 컨텍스트 확인
```shell
k config get-contexts
```
# docker image 생성
```shell
sudo docker build -t airflow-local:2.10.5 .
```

# kind에 docker image load
```shell
kind load docker-image airflow-local:2.10.5 --name airflow-local
```

# Helm repo 등록 & 업데이트
```shell
helm repo add airflow https://airflow.apache.org
helm repo update
```

# airflow 설치
```shell
helm install airflow airflow/airflow \
    --namespace airflow \
    --create-namespace \
    -f app-chart/airflow/values.yaml \
    -f app-chart/airflow/values-local.yaml \
    -f app-chart/airflow/values-secret.yaml
```

# 설치 확인 & 접속
```shell
# pod 상태 확인
kubectl get pods -n airflow
```

```
# 웹 UI 포트포워딩
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow
```

### helm 차트 업데이트 반영
```shell
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace -f values.yaml --debug
```

### pod 접속
```shell
k exec -it airflow-scheduler-699495d87-dtx94 --namespace airflow -- /bin/bash
```

### crash 날 땐 
```text
pvc 전체 삭제 후 실행
```
### helm upgrade 문제가 생겼다면 rollback 
```shell
helm rollback airflow 1 -n airflow
```
