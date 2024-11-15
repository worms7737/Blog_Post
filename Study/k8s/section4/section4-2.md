https://192.168.56.31:30000/#/create?namespace=_all

url 접속 후 우측 상단 + 버튼으로 파드 생성하기

apiVersion: v1
kind: Pod
metadata:
  name: pod-1
spec:
  containers:
  - name: container1
    image: kubetm/p8000
    ports:
    - containerPort: 8000
  - name: container2
    image: kubetm/p8080
    ports:
    - containerPort: 8080

!!! namespace default로 실습중 !!!

curl <ip>:8080
curl <ip>:8000

