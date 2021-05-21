# 영화 추천 프로젝트

사용 기술 스택

프론트 : Vue.js
백 : Django
DB : SQLlite
Infra : Docker

# 사용법

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8b32be22-a86f-423d-b6fc-1f94a86ff386/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8b32be22-a86f-423d-b6fc-1f94a86ff386/Untitled.png)

로그인후 영화 목록을 누르면 다양한 최신 영화들의 리스트가 나옴

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c36f8335-8154-4382-a043-190ddd01728b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c36f8335-8154-4382-a043-190ddd01728b/Untitled.png)

추천 영화를 클릭하면

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32f77008-8941-4887-a897-1f5efdbbceae/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32f77008-8941-4887-a897-1f5efdbbceae/Untitled.png)

가입시 선택한 취향과 그동안 봐왔던 영화를 기반으로 영화를 추천해줌

마이페이지에서

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b2875b8-8b58-47bb-b6a1-c0bc87e94f8d/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b2875b8-8b58-47bb-b6a1-c0bc87e94f8d/Untitled.png)

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