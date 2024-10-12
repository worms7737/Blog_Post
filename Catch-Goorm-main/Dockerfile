# Python 3.9 이미지를 기반으로 함
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 설치
# Pillow와 mysqlclient를 설치할 수 있도록 추가 패키지 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# pip 업그레이드
RUN python -m pip install --upgrade pip

# 필요 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 컨테이너 실행 시 Django 서버를 Gunicorn으로 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "User_service.wsgi:application"]
