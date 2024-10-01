Github Actions란 무엇인가?
Workflows란?
Jobs란?
Steps란?
Actions란?
with

워크플로우 파일 작성 방법
name
on
runs-on
steps

Actions 시나리오 탐색
checkout
cache

Jobs 심화
작업 실행 순서 제어
작업 간 output 전달
선택적 작업 실행

그 외(추가 가능)
참고 자료: https://docs.github.com/ko/actions

---

# GitHub Actions 이해

## 개요

---

GitHub Actions는 빌드, 테스트 및 배포 파이프라인을 자동화할 수 있는 CI/CD(연속 통합 및 지속적인 업데이트) 플랫폼임. 리포지토리에 대한 모든 Pull 요청을 빌드 및 테스트하거나 병합된 Pull Request 를 프로덕션에 배포하는 워크플로를 만들 수 있음.

GitHub Actions은(는) 단순한 DevOps 수준을 넘어 리포지토리에서 다른 이벤트가 발생할 때 워크플로를 실행할 수 있도록 함. 예를 들어 누군가가 리포지토리에서 새 이슈를 만들 때마다 워크플로를 실행하여 적절한 레이블을 자동으로 추가할 수 있음.

## Workflow

---

*Workflow* 는 하나 이상의 작업을 실행할 구성 가능한 자동화된 프로세스임. 워크플로는 리포지토리에 체크인된 YAML 파일에서 정의되며, 리포지토리의 이벤트로 트리거될 때 실행되거나 수동으로 또는 정의된 일정에 따라 트리거될 수 있음.

*Workflow*는 리포지토리의 .github/workflows 디렉터리에 정의됨. 리포지토리에 다음과 같은 각각의 다른 작업 집합을 수행하는 여러 워크플로가 있을 수 있음.

- Pull Request를 빌드하고 테스트함.
- 릴리스가 생성될 떄마다 애플리케이션을 배포함.
- 새 문제가 보고될 때마다 레이블을 추가함.

다른 워크플로 내에서 워크플로를 참조할 수 있음.

## Jobs

---

*Jobs*란 독립된 가상 머신(machine) 또는 컨테이너 (container)에서 돌아가는 하나의 처리 단위를 의미합니다. 하나의 워크플로우는 여러 개의 작업으로 구성되며 적어도 하나의 작업은 있어야 함. (아니라면 실행할 작업이 없으니 워크플로우가 의미가 없어짐) 모든 작업은 기본적으로 동시에 실행되며 필요 시 작업 간에 의존 관계를 설정하여 작업이 실행되는 순서를 제어할 수도 있음.

작업은 워크플로우 YAML 파일 내에서 *jobs* 속성을 사용하며 작업 식별자(ID)와 작업 세부 내용 간의 맵핑(Mapping) 형태로 명시가 됨.

***.github/workflows/example.yml
```
# ...(생략)...

jobs:
    job1:
        # job1에 대한 세부 내용
        runs-on: ubuntu-latest
    job2:
        # job2에 대한 세부 내용
    job3:
        # job3에 대한 세부 내용
```
예를 들어, 가장 널리 사용되는 우분투의 최신 실행 환경에서 해당 작업을 실행하고 싶다면 다음과 같이 설정합니다.

## Steps

---

정말 단순한 작업이 아닌 이상 하나의 작업은 일반적으로 여러 단계의 명령을 순차적으로 실행하는 경우가 많음. 
-> Github Actions 에서는 각 작업 (job)이 하나 이상의 단계(step)로 모델링이 됨.

작업 단계는 단순한 커맨드(command)나 스크립트(script)가 될 수도 있고 다음 섹션에서 자세히 설명할 액션(action)이라고 하는 좀 더 복잡한 명령일 수도 있음.
커맨드나 스크립트를 실행할 때는 ~run~ 속성을 사용하며, 액션을 사용할 때는 ~uses~ 속성을 사용함.

예를 들어, 자바스크립트 프로젝트에서 테스트를 돌리려면 코드 저장소에 코드를 작업 실행 환경을 내려 받고, 패키지를 설치한 후, 테스트 스크립트를 실행해야 함.
이 3단계의 작업을 ~steps~ 속성을 통해 명시.

```
# ...(생략)...

jobs:
    test:
        runs-on: ubuntu-latest
        steps:
            - uses: actioins/checkout@v3
            - runs: npm install
            - runs: npm test
```

## Actions

---

~Actions~은 Github Actions에서 빈번하게 필요한 반복 단계를 재사용하기 용이하도록 제공되는 일종의 작업 공유 메커니즘임. 이 액션은 하나의 코드 저장소 범위 내에서 여러 워크플로우 간에서 공유를 할 수 있을 뿐만 아니라, 공개 코드 저장소를 통해 액션을 공유하면 Github 상의 모든 코드 저장소에서 사용이 가능해짐.

Github에서 제공하는 대표적인 공개 액션으로 바로 위 예제에서도 사용했던 체크 아웃 액션(actions/checkout) 을 들 수 있음. 대부분의 CI/CD 작업은 코드 저장소로 부터 코드를 작업 실행 환경으로 내려받는 것으로 시작되므로 이 액션이 얼마나 범용적으로 사용될지는 굳이 말할 필요가 없음.

뿐만 아니라 Github Marketplace에서는 수많은 벤더(vendor)가 공개해놓은 다양한 액션을 쉽게 접할 수 가 있음. 이 액션을 중심으로 하나의 큰 커뮤니티가 형성되고 더 많은 사용자와 벤더가 Github Actions로 몰려드는 선순환이 발생.
---

# 워크플로우 작성 방법

~.yml~ 워크플로 파일은 YAML 구문을 사용하거나 파일 확장자가 있어야 함. ~.github/workflows~ 워크플로 파일은 저장소 디렉토리에 저장해야 합니다.

## name
---
- 워크플로 이름. GitHub는 리포지토리의 "Actions" 탭 아래에 워크플로 이름을 표시함. 

## on: [push]
---

- 해당 workflow에 대한 Trigger를 지정.
- 리포지토리에 변경사항을 push할 때 마다 workflow 실행이 trigger 된다.
- 특벙 분기, 경로 또는 태그에 대해 제한을 걸 수도 있는 등, trigger를 다양하게 구성할 수 있다.

```
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```



## jobs:
---

- 해당 workflow에서 발생하는 작업을 그룹화한다.

## runs-on: 
---

- GitHub에서 제공(호스팅)하는 새로운 가상 머신에서 실행 됨을 의미함.

```

runs-on: ubuntu-latest

# 여러 운영체제에서 실행할 경우 배열로 나열 가능
runs-on: [ubuntu-latest, windows-latest, macos-latest] 

```

## steps:
---

- 작업(jobs)에서 실행되는 모든 단계를 그룹화
- 해당 섹션 아래의 항목: 별도의 작업 or Shell Script

```
steps:
  - name: Checkout repository
    uses: actions/checkout@v2
  
  - name: Set up Node.js
    uses: actions/setup-node@v2
    with:
      node-version: '14'

  - name: Install dependencies
    run: npm install

  - name: Run tests
    run: npm test
```

# Actions 시나리오 탐색

## checkout 액션
---

- **actions/checkout**은 GitHub Actions에서 워크플로우를 실행할 때, 리포지토리의 소스 코드를 가져오는 역할을 합니다. 기본적으로, GitHub Actions 워크플로우가 실행될 때, 워크플로우는 가상 머신에서 실행되며, 소스 코드가 그 가상 머신에 로드되어 있지 않기 때문에 소스를 직접 체크아웃해야 합니다.

- 이 액션은 리포지토리의 코드(특정 브랜치, 커밋 또는 태그)를 가져와 워크플로우의 후속 단계에서 사용할 수 있도록 합니다.

```

steps:
    - name: Checkout code
      uses: actions/checkout@v2

# 위 코드는 현재 리포지토리의 최신 소스 코드를 기본 브랜치로부터 체크아웃함.
# v2 는 액션의 버전을 의미하며, 안정된 버전 중 하나임.


# ref: 체크아웃할 브랜치, 태그, 커밋 등을 지정할 수 있음.
steps:
  - name: Checkout specific branch
    uses: actions/checkout@v2
    with:
      ref: feature-branch

# fetch-depth: 커밋 히스토리를 어느 정도까지 가져올지 설정합니다. 기본값은 1로, 최신 커밋만 가져옴.
steps:
  - name: Checkout entire history
    uses: actions/checkout@v2
    with:
      fetch-depth: 0
# fetch-depth: 0으로 설정하면 전체 커밋 기록을 가져옴.

```

** 실제 사용 시나리오: **

- CI 파이프라인에서 코드를 빌드, 테스트, 배포하려면 소스 코드를 가져와야 함. 이때 checkout 액션이 필수적으로 사용됨.
- 특정 브랜치나 태그에 기반한 작업을 진행할 때도 checkout 액션을 통해 필요한 코드를 가져옴.

## cache 액션
---

- **actions/cache**는 워크플로우에서 종속성 파일이나 빌드 결과 등을 캐싱하여 빌드 시간을 단축시키는 액션입니다. 이 액션은 종속성을 매번 다시 설치할 필요 없이, 이전 실행에서 생성된 데이터를 저장하고 다시 사용할 수 있도록 합니다.

- 빌드나 테스트 속도를 크게 향상시키는 데 도움을 줍니다. 특히 Node.js, Python, Java 등의 프로젝트에서 패키지 매니저의 종속성 설치에 대한 캐시를 사용하면 유용합니다.

```

steps:
  - name: Cache Node.js dependencies
    uses: actions/cache@v3
    with:
      path: node_modules
      key: ${{ runner.os }}-node-${{ hashFiles('package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-node-

````

- 이 코드는 Node.js의 node_modules 디렉토리를 캐싱하여, 다음 실행에서 캐시된 종속성을 사용합니다. package-lock.json 파일의 해시 값이 캐시의 키로 사용됩니다.
- restore-keys는 캐시를 복원할 때 사용할 대체 키로, 키가 일치하지 않을 때 가장 비슷한 캐시를 찾아 복원합니다.

---

** 주요 옵션 **

- path: 캐시할 디렉토리 또는 파일의 경로를 지정함.
  - 예: node_modules, ~/.m2/repository, ~/.cache/pip 등.
- key: 캐시 키로 사용될 문자열을 지정합니다. 일반적으로 OS와 종속성 파일의 해시 값 등을 포함.

```

with:
  key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

```







