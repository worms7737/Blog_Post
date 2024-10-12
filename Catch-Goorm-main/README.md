# First-Django-Project
캐치구름 조의 첫번째 Django 와 Docker 를 활용한 프로젝트입니다

## 필수 패키지

이 프로젝트는 특정 Python 패키지에 의존합니다. 패키지 의존성을 관리하기 위해 `requirements.txt` 파일을 사용하고 있습니다.

## 가상 환경 설정

프로젝트의 패키지와 의존성을 독립적으로 관리하기 위해 가상 환경을 사용하는 것이 좋습니다. 가상 환경을 생성하고 활성화하는 방법은 다음과 같습니다:

### 가상 환경 생성 및 활성화

1. **가상 환경 생성:**

   ```bash
   python -m venv venv
   ```

2. **가상 환경 활성화:**

   - **Windows:**

     ```bash
     .\venv\Scripts\Activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

## 패키지 설치....

가상 환경을 활성화한 후, `requirements.txt` 파일을 사용하여 필요한 패키지를 설치할 수 있습니다. 다음 명령어를 사용하여 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

## 브랜치 전략 <Git Flow의 경량 버전>
1. Main 브랜치는 완성된 코드만 유지한다.
2. Develop 브랜치는 개발 프레임워크를 제공한다. 해당 코드를 기반으로 작업한다.
3. Develop 브랜치 하위에 [개인 이름_Feature] 브랜치를 생성한다. 해당 브랜치에서 각자 업데이트를 위한 코드를 작성한다.

예시) 

<img width="599" alt="image" src="https://github.com/user-attachments/assets/7e5d81a4-abc0-40ac-9a72-3dc74f2a575a">


test
