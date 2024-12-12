## conda 설치
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

## conda로 가상환경 구성
source ~/miniconda3/bin/activate
conda init --all

conda create -n [vm_name] python=[버전 명시]
conda activate vm_name

## Fast api 설치
pip install fastapi==0.111.1

## VSCODE 사용시
Cmd + Shift + P 후 python interpreter 를 통해 생성한 venv로 인터프리터 생성

## default 로 주기


---

## fastapi 구동해보기
uvicorn main:app --port=8081 --reload
>main: 파일 이름
>app: fastapi 인스턴스 이름
>--reload: 소스 변경 사항이 자동 반영되는 옵션