# 영화 추천 프로젝트

사용 기술 스택

프론트 : Vue.js
백 : Django
DB : SQLlite
Infra : Docker

# 사용법

![K-009](/uploads/aa5c23feae0e3a333915962d181018fc/K-009.png)

로그인후 영화 목록을 누르면 다양한 최신 영화들의 리스트가 나옴

![K-010](/uploads/fe6d472baaa7b0df01c5d21a1738bcbc/K-010.png)

추천 영화를 클릭하면

![K-011](/uploads/8c80f07769d31a274cb54482138d3ad4/K-011.png)

가입시 선택한 취향과 그동안 봐왔던 영화를 기반으로 영화를 추천해줌

마이페이지에서

![K-012](/uploads/b352f09405904010e4da78d3be20d3a6/K-012.png)

그동안 봐웠던 영화에 대한 선호도를 알 수 있음

# 배포 방법

ec2 접속후

관리자 명: ubuntu

프론트 도커 빌드 및 실행
docker build --tag frontimage s04p31d108/frontend/movie/
docker run -dit -p 80:80 --name frontsite frontimage

백 도커 빌드 및 실행
docker build --tag backimage s04p31d108/backend/
docker run -dit -p 8000:8000 --name backsite backimage

DB파일은 backend 폴더안에 있음