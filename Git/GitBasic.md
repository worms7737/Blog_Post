# Git 정리 

## Git?

> **Git** 은 분산 버전 관리 시스템으로써 소프트웨어 개발 프로젝트(코드)의 변화를 추적한다. **Git**은 개발자들간의 조직화, 협업, 속도, 효율성을 높히는 목적으로 쓰인다.

**깃허브(GitHub)**는 Git을 사용하는, 웹에서 호스팅하는 버전 관리 시스템이다. **깃허브**는 분산된 버전 관리 기능을 제공하고 Git의 소스 코드(source code) 관리 기능을 포함한 여러가지 다른 기능들을 제공한다.

## Git 설치

** Windows **
 - https://git-scm.com/downloads
 - Git Bash에 체크

** Mac OS **
 - Hombebrew 설치: https://brew.sh/
    - brew: Mac 터미널 기반 패키지 관리 프로그램
        - homebrew: "직접 담근 술"
```
brew install git
```

---

## git init

- 프로젝트 소스코드를 git을 이용하여 버전 관리를 하고자 한다면, 관리가 필요한 범위의 디렉토리에서 git init 명령을 수행해야 한다.
- init의 위치는 중요하다. 새로 생성하는 프로젝트 별로 init을 수행해줘야 한다.

```
mkdir git-practice
cd git-practice
ls -al

git init
ls -al #.git 폴더 생성
# .git 폴더는 버전 관리에 필요한 것들을 모아놓은 숨겨진 디렉토리이다.
```
## 로컬에서 새로 작업한다면?
```
echo "#git-practice" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
# 현재 브랜치의 이름을 'main'으로 변경합니다.
# Git의 기본 브랜치 이름을 'main'으로 설정합니다 (예전에는 'master'가 기본이었음).

git remote add origin <레포주소>
# 원격 저장소(origin)를 추가합니다. 여기서 <레포주소>는 GitHub 등의 원격 저장소 주소입니다.
# 이 명령어는 로컬 저장소와 원격 저장소를 연결하는 역할을 합니다.

git push -u origin main
# 로컬 저장소의 'main' 브랜치에 있는 커밋을 원격 저장소(origin)의 'main' 브랜치로 푸시합니다.
# '-u' 옵션은 이 로컬 브랜치와 원격 브랜치를 추적 관계로 설정하므로, 다음부터는 'git push'만 입력하면 됩니다.
```

## 로컬에 이미 작업중인 프로젝트를 연결하려면
```
git remote add origin [git ssh 주소]
git branch -M main
git push -u origin main
```

---

## Github 과의 Secure 통신 설정

** [선택1] SSH 세팅 **
``` 
ssh-keygen

#공개키를 저장하고 있는 파일: ~/.ssh/id_rsa.pub

cat ~/.ssh/id_rsa.pub

# 공개키를 github에게 넘겨줘야 한다.
# key 값을 첫 글자부터 끝 글자까지만 복사 -> github -> 프로필 settings -> SSH and GPG keys -> new ssh key -> Title: 임의 Key: 붙여넣기
```

** [선택2] Github Credential 발급 **

- 프로필 Settings -> Developer settings -> Personal access token -> Tokens(classic) -> Generate new token -> Generate new toekn[classic] -> Note는 기억하기 쉬운 이름으로 설정, Expiration으로 만료날짜 지정, Select scopse로 권한 설정 -> Generate Token

- ghp_ ... 로 시작하는 토큰을 복사하여 따로 보관/저장 -> 유출되지 않도록 주의
- [권장하지 않음] commit, push 할 때 마다 암호 입력이 귀찮기 때문
```
git config --global credentail.helper store
```

---

## 작업 흐름
파일 수정 -> ~git status~로 commit 대상 파일을 확인 -> ~git add~ 로 staging 영역에 추가 -> ~git commit~ -> ~git status~로 상태 확인 -> ~git log~ 로 commit 히스토리 확인

**Git의 3가지 작업 영역**
git은 기본적으로 세 가지 작업 영역을 가진다.
- workiing directory (working tree)
- staging 영역
- repository

~git add~ , ~git commit~ , ~git push~, ~git pull~, 등 git 전반에 걸쳐 내재되어 있는 개념으로서, 이해가 안되면 외우시는 걸 추천 (면접에는 안나옴!)

---



## git clone
기본적으로 git은 리포지토리(Repository)에서 버전 관리를 할 수 있게 해준다.

```
git clone git@github.com:worms7737/Blog_Post.git
```

