import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
// import { loginUser, fetchUser } from '@/api/auth';
// import router from '../router/index';
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: '',
    email: '',
    password: '',
    uuid: '',
    nowPlaying: [],
    popular: [],
    upComing: [],
  },
  getters: {
    isLogin(state) {
      return state.token !== '';
    },
  },
  mutations: {
    //토큰
    setToken(state, token) {
      state.token = token;
    },
    clearToken(state) {
      state.token = '';
    },
    //이메일
    setEmail(state, email) {
      state.email = email;
    },
    clearEmail(state) {
      state.email = '';
    },
    setPassword(state, password) {
      state.password = password;
    },
    clearPassword(state) {
      state.password = '';
    },
    setUuid(state, uuid) {
      state.uuid = uuid;
    },
    clearUuid(state) {
      state.uuid = '';
    },
    SET_LOADING(state, data) {
      state.loading = data;
    },
    SET_NOW_PLAYING(state, data) {
      state.nowPlaying = data;
    },
    SET_POPULAR(state, data) {
      state.popular = data;
    },
    SET_UP_COMING(state, data) {
      state.upComing = data;
    },
  },

  actions: {
    // async LOGIN({ commit }, userData) {
    // const data = await loginUser(userData);
    // console.log(data);
    // if (data.data.message == 'SUCCESS') {
    //   commit('setToken', data.data['access-token']);
    //   commit('setEmail', userData.email);
    //   commit('setPassword', userData.password);
    //   commit('setUuid', response.data.uuid);
    //   router.push('/main');
    // } else {
    //   Vue.swal({
    //     icon: 'error',
    //     title: '로그인 실패! 이메일 및 비밀번호를 확인해 주세요!',
    //   });
    // },
  },
});
