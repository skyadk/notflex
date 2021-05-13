import { instance, posts } from './index';

// 로그인
function loginUser(userData) {
  return instance.post('', userData);
}
// 사용자정보조회
function fetchUser(email) {
  return posts.get(``);
}
//회원가입
function register(userData) {
  return instance.post('', userData);
}
//정보수정
function editUser(userData) {
  return posts.put(``, userData);
}
//회원탈퇴
function signout(email) {
  return posts.delete(`/'`);
}

export { loginUser, fetchUser, register, editUser, signout };
