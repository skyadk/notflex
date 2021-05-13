import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import { loginUser } from '@/api/auth';
import router from '../router/index';
Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: '',
    email: '',
    password: '',
    uuid: '',
    nickname: '',
    preferGenre: '',
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
    setNickname(state, nickname) {
      state.nickname = nickname;
    },
    clearNickname(state) {
      state.nickname = '';
    },
    setPreferGenre(state, preferGenre) {
      state.preferGenre = preferGenre;
    },
    clearsetPreferGenre(state) {
      state.preferGenre = '';
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
    async LOGIN({ commit }, userData) {
      const data = await loginUser(userData.email);
      console.log(data);
      if (data.password == userData.password) {
        commit('setEmail', data.email);
        commit('setPassword', data.pw);
        commit('setUuid', data.id);
        commit('setNickname', data.nickname);
        commit('setPreferGenre', data.preferGenre);
        router.push('/');
      } else {
        Vue.swal({
          icon: 'error',
          title: '로그인 실패! 이메일 및 비밀번호를 확인해 주세요!',
        });
      }
    },
  },
});
