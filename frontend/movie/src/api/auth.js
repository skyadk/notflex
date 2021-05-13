import { instance, posts } from './index';

// 로그인
function loginUser(userData) {
  return instance.post('get_user/', userData);
}

//회원가입
function register(userData) {
  return instance.post('join_user/', userData);
}
//정보수정
function editUser(userData) {
  return posts.put(``, userData);
}
//회원탈퇴
function signout() {
  return posts.delete(`/'`);
}

export { loginUser, register, editUser, signout };
