echo '======== [1-1] 패키지 업데이트 ========'
sudo apt-get update -y && sudo apt-get upgrade -y

echo '======== [1-2] 타임존 설정 ========'
sudo timedatectl set-timezone Asia/Seoul

echo '======== [1-3] Git 설치 ========'
sudo apt install git-all


echo '======== [2-1] Docker 설치 ========'
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

echo '======== [2-2] Docker 설치 ========'
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo '======== [2-3] Docker Compose 설치 ========'
sudo apt-get update
sudo apt-get install docker-compose-plugin

# 프로젝트 클론 
git clone [git@github.com:worms7737/load_test.git] 
cd bootcampchat 
# 백엔드 패키지 설치 
cd backend 
npm install 
# 프론트엔드 패키지 설치 
cd ../frontend 
npm install