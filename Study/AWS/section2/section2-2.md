# Network

## Network Layer

- 여러 노드의 경로를 찾고 올바르게 전달 될 수 있는 기능과 수단을 정의
- 주요 단위: 패킷
- 주요 구성 요소
    - ** Route, IP, ARP **
- 주요 특징
    - 서로 떨어진 Local Network 간의 통신을 지원
    - "Network 간의" -> Inter Network -> Internet
    - 중간중간 Node들을 거쳐서 목적지 까지 도달할 수 있는 방법을 지원

---

## IP(internet protocol) Address

- internet protocol상에서 통신 주체를 식별하기 위한 아이디
- 두가지 종류
    - IPv4 : 32Bits (2^32 = 약 43억개)
        - 아이피를 최대로 활용하기 위해 사설(private) ip 와 공인(public) ip 로 분류
    - IPv6 : 128Bits (2^128)
        - IPv4 보다 훨~씬 더 많음
        - 따라서 사설ip 개념 불필요
    MAC Address와 다르게 수시로 변동 가능

---

### Classless Inter Domain Routing(CIDR)

- IP는 주소의 영역을 여러 네트워크 영역으로 나누기 위해 IP를 묶는 방식
- 여러 개의 사설망을 구축하기 위해 망을 나누는 방법

### CIDR Notation

- IP 주소의 **집합**
- 네트워크 주소와 호스트 주소로 구성
- 각 호스트 주소 숫자 만큼의 아이피를 가진 네트워크 망 형성 가능
- A.B.C.D/E 형식
    - 예: 10.0.1.0/24 , 172.16.0.0/12
    - A,B,C,D : 네트워크 주소 + 호스트 주소 표시
    - E : 0~32, 네트워크 주소가 몇 bit 인지 표시

---

