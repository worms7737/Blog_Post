# Introduction 

본 실습 과정은 AWS Training and Certification을 바탕으로 작성되었습니다.

# 사례

<p align="center">
  <img src="https://velog.velcdn.com/images/rockwellvinca/post/2ec81df8-f8d5-4d07-a30e-b76dc86ba9bb/image.png" alt="대표 이미지" />
</p>

## 어떤 요소가 있을까?

- vpc
- 인터넷 게이트웨이
- 인터넷으로의 퍼블릭 경로가 포함된 라우팅 테이블
- 기용 영역(AZ) 2개
- 퍼블릭 서브넷 2개

## 🌎 VPC 란?

### Amazon Virtual Private Cloud

AWS에서 제공하는 **가상 네트워킹 환경**으로, **클라우드에서 자체 전용 네트워크를** 만들 수 있는 서비스이다.

VPC를 사용하면 AWS 클라우드 내에서 리소스를 **VPC 내로 격리**하고, 사용자가 정의한 가상 네트워크 환경에서 작동할 수 있도록 한다.

이를 통해 기업이나 조직은 클라우드 리소스를 보다 **안전하게 관리하고 사용할 수 있다.**

### 인터넷 게이트웨이란?

AWS VPC에서 **인터넷과의 통신**을 가능케 하는 필수적인 구성 요소.
이 게이트웨이를 통해 VPC 내의 리소스들이 **외부의 인터넷과 통신**할 수 있다.

간단하게 설명하자면, 인터넷 게이트웨이는 VPC 내의 **프라이빗 네트워크와 외부의 공개된 인터넷 간에 통로 역할**을 수행한다.

이를 통해 VPC 내부의 인스턴스들이 외부의 서비스에 접근하거나 외부에서 VPC 내부의 리소스에 접근할 수 있게 도와준다.

## VPC 생성


