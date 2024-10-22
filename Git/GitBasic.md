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
    - 말 그대로 작업 디렉토리이며, 실제 프로젝트의 위치라고 할 수 있음.
- staging 영역
    - ~git add~ 한 파일들이 스테이지에 추가된다. commit 명령을 실행하면, staging 영역에 있는 파일들만 commit 된다.
- repository
    - 버전 관리 시스템이 변경 사항을 영구적으로 저장하는 곳이다.

`git add` , `git commit` , `git push`, `git pull`, 등 git 전반에 걸쳐 내재되어 있는 개념으로서, 이해가 안되면 외우시는 걸 추천 (면접에는 안나옴!)

---

## git status
현재 *작업 디렉토리*의 상태를 보여준다.

어떤 파일이 변경, 스테이징, 추적되지 않고 있는지 확인이 가능하다.

```
git status
```

---

## git log
이제까지 commit 된 이력 또는 내역을 보여준다.

```
git log
```

---

## git remote
commit들(저장본들)이 존재하는 Local repository의 내용을  Remote repository와 연결하기 위해 사용된다.

💡 `origin`
- `origin은 Git에서 원격 저장소를 가리키는 이름으로 자주 사용되는 관용적인 명칭이다. 따라서 다른 이름으로도 사용가능.
- 예를 들어, 원격 저장소가 배포 서버라면 `production`이라고 할 수도 있고, 그냥 원격 github repository를 의미하는 remote라는 명칭을 쓸 수 도 있다.
- 이 명칭은 `push`,`pull`,`fetch` 때에 쓰인다.
- 보통은 관례적인 표현인 `origin` 을 사용한다.

---

## git push
로컬 저장소에 있는 변경 사항을 원격 저장소에 업로드하는 git 명령.
기본적인 `git push 명령은 다음과 같은 구조를 가진다.
```
git push [원격 저장소 이름: 관용적으로 origin] [로컬브랜치이름]:[원격브랜치이름]
```

`git push`를 실행하기 전에 로컬 저장소와 원격 저장소가 동기화되어 있어야 한다.
동기화되지 않은 경우에는 `git pull` 명령을 사용하여 원격 저장소의 최신 변경 사항을 가져온 후에 `git push` 를 실행해야 한다

---

## git pull



## git clone
기본적으로 git은 리포지토리(Repository)에서 버전 관리를 할 수 있게 해준다.

```
git clone git@github.com:worms7737/Blog_Post.git
```

