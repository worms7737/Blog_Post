# OSI 7 Layer Model

## Physical Layer

- 장치를 연결하기 위한 매체의 물리적인 사항을 정의
    - 전압, 주기, 시간, 전선의 규격, 거리 등
- 주요 단위: Bits
- 대표 구성 요소
    - 케이블/안테나/RF등 전송 매체, **허브, 리피터**

하나하나를 관리하기는 매우 힘들다.
-> Hub의 등장

## Hub

- Physical Layer 단위에서 다수의 기기들을 연결해주는 장치
- 특징
    - 에러 / 충돌(Collsion) / 디바이스 별 제어 기능 없음
    - 받은 내용을 그대로 전달 -> 무조건 Broadcast
> 각 클라이언트가 보낸 요청을 그대로 전달하는 역할 ( 일종의 확성기 )

모두가 요청을 보내는 상황 == 충돌(collision) 발생

### Pysical Layer 에서 해결하지 못한 문제

- 충돌
- Broadcast만 가능 -> 대상을 지정해서 전달 불가능

---

## Data Link Layer

- 물리적인 통신을 제어하며 디바이스와 디바이스 간의 통신 및 전송을 안정화 하기 위한  프로토콜
- 주요 단위: Frame
- 주요 구성 요소
    - ** Mac Address, Switch **
- 주요 특징
    - CSMA/CD(Carrier-Sense Multiple Access with Collision Detection) 방식을 활용해서 각 디바이스 간의 통신을 원활하게 연결
    - 대상을 구별하여 디바이스간의 통신을 지원(Unicast)
        - Broadcast도 지원

> Mac Address
  - 네트워크 인터페이스에 부여된 고유의 주소
    -데이터가 지정한 대상에게 잘 전달될수 있도록 대상 식별에 사용
  - 2개의 Hexadeciaml 단위로 6개를 나열 = 48bits = 6bytes
  - 두 파트로 구분
    - 첫 3개의 bytes는 OUI: 제조사에 부여된 고유 식별자
    - 나머지 3개의 byte는 NIC: 네트워크 인터페이스 별 고유 번호
  - ** 네트워크 인터페이스의 Mac Address는 고유의 값이며 변하지 않음 **
    - IP는 변동

### Data Link Layer 해결하지 못한 문제

- 로컬 네트워크 외부로 통신 불가능