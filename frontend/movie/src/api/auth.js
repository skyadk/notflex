import { instance } from './index';

// 로그인
function loginUser(userData) {
  return instance.post('get_user/', userData);
}

//회원가입
function register(userData) {
  return instance.post('join_user/', userData);
}

export { loginUser, register };
